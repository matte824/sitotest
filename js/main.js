/* ==========================================================================
   main.js — nav, reveal, canvas hero (con interazione mouse), contatori, form
   ========================================================================== */

(function () {
  "use strict";

  /* ---------- 1. NAV ---------- */
  const nav = document.getElementById("nav");
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");

  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 40);
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      const open = navLinks.classList.toggle("is-open");
      navToggle.classList.toggle("is-open", open);
      navToggle.setAttribute("aria-expanded", open);
      document.body.style.overflow = open ? "hidden" : "";
    });
    navLinks.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        navLinks.classList.remove("is-open");
        navToggle.classList.remove("is-open");
        document.body.style.overflow = "";
      })
    );
  }

  // Evidenzia la voce di menu della pagina corrente
  const current = location.pathname.split("/").pop() || "index.html";
  navLinks.querySelectorAll("a").forEach((a) => {
    if (a.getAttribute("href") === current) a.classList.add("is-active");
  });

  /* ---------- 2. REVEAL ON SCROLL ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------- 3. CANVAS HERO: costellazione con interazione mouse ---------- */
  const canvas = document.getElementById("heroCanvas");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (canvas && !reduceMotion) {
    const ctx = canvas.getContext("2d");
    let w, h, nodes, raf;
    const DPR = Math.min(window.devicePixelRatio || 1, 2);
    const mouse = { x: -9999, y: -9999 };

    const resize = () => {
      w = canvas.offsetWidth;
      h = canvas.offsetHeight;
      canvas.width = w * DPR;
      canvas.height = h * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      initNodes();
    };

    const initNodes = () => {
      const count = Math.min(Math.floor((w * h) / 14000), 110);
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.32,
        vy: (Math.random() - 0.5) * 0.32,
        r: Math.random() * 1.7 + 0.7,
      }));
    };

    const LINK = 150;
    const MOUSE_LINK = 210;

    const draw = () => {
      ctx.clearRect(0, 0, w, h);

      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];
        n.x += n.vx;
        n.y += n.vy;
        if (n.x < 0 || n.x > w) n.vx *= -1;
        if (n.y < 0 || n.y > h) n.vy *= -1;

        // Linee tra nodi vicini (oro, ben visibili)
        for (let j = i + 1; j < nodes.length; j++) {
          const m = nodes[j];
          const dist = Math.hypot(n.x - m.x, n.y - m.y);
          if (dist < LINK) {
            const alpha = (1 - dist / LINK) * 0.28;
            ctx.strokeStyle = `rgba(200, 169, 110, ${alpha})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(m.x, m.y);
            ctx.stroke();
          }
        }

        // Connessione luminosa verso il cursore
        const md = Math.hypot(n.x - mouse.x, n.y - mouse.y);
        if (md < MOUSE_LINK) {
          const alpha = (1 - md / MOUSE_LINK) * 0.5;
          ctx.strokeStyle = `rgba(227, 201, 143, ${alpha})`;
          ctx.lineWidth = 1.1;
          ctx.beginPath();
          ctx.moveTo(n.x, n.y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.stroke();
        }

        // Nodo con leggero glow
        ctx.fillStyle = "rgba(242, 239, 233, 0.55)";
        ctx.shadowColor = "rgba(200, 169, 110, 0.8)";
        ctx.shadowBlur = 6;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }
      raf = requestAnimationFrame(draw);
    };

    const hero = canvas.closest(".hero");
    hero.addEventListener("pointermove", (e) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });
    hero.addEventListener("pointerleave", () => { mouse.x = -9999; mouse.y = -9999; });

    // Anima solo quando visibile (batteria mobile)
    const heroObserver = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) raf = requestAnimationFrame(draw);
      else cancelAnimationFrame(raf);
    });

    resize();
    heroObserver.observe(canvas);
    window.addEventListener("resize", resize);
  }

  /* ---------- 4. CONTATORI ---------- */
  const counters = document.querySelectorAll("[data-count]");
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.count, 10);
    const suffix = el.dataset.suffix || "";
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / 1400, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (counters.length && "IntersectionObserver" in window) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { animateCounter(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach((c) => cio.observe(c));
  }

  /* ---------- 5. FORM (Formspree → matteo.notario@pfafineco.it) ---------- */
  const form = document.getElementById("contactForm");
  const status = document.getElementById("formStatus");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      btn.textContent = "Invio in corso…";
      try {
        const res = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
        });
        if (!res.ok) throw new Error();
        form.reset();
        status.textContent = "Richiesta inviata. Ti ricontatto entro 24 ore lavorative.";
        btn.textContent = "Inviata ✓";
      } catch {
        status.textContent = "Si è verificato un problema. Scrivimi a matteo.notario@pfafineco.it";
        btn.disabled = false;
        btn.textContent = "Invia la richiesta";
      }
    });
  }


  /* ==========================================================================
     CALCOLATORI — nessuna libreria esterna, nessun dato inviato: tutto nel browser
     Metodologia interesse composto coerente con il Calcolatore dell'interesse
     di Banca d'Italia: capitalizzazione mensile, versamenti a fine periodo.
     ========================================================================== */
  const fmtEUR = (n) => Math.round(n).toLocaleString("it-IT") + " \u20AC";

  // Collega slider + campo numerico: restituisce un getter del valore corrente.
  // Il campo a mano puo' superare il massimo dello slider (nessun tetto rigido).
  const bindControl = (id, onChange) => {
    const range = document.getElementById(id);
    const num = document.getElementById(id + "Num");
    if (!range || !num) return null;
    const setFill = () => {
      const p = ((range.value - range.min) / (range.max - range.min)) * 100;
      range.style.setProperty("--fill", Math.min(Math.max(p, 0), 100) + "%");
    };
    range.addEventListener("input", () => { num.value = range.value; setFill(); onChange(); });
    num.addEventListener("input", () => {
      const v = parseFloat(num.value);
      if (isNaN(v)) return;
      range.value = Math.min(Math.max(v, range.min), range.max);
      setFill(); onChange();
    });
    setFill();
    return () => {
      const v = parseFloat(num.value);
      return isNaN(v) ? parseFloat(range.value) : v;
    };
  };

  /* ---------- Calcolatore 1 (homepage): inflazione sul capitale fermo ---------- */
  if (document.getElementById("infCap")) {
    let gCap, gYears, gRate;
    const update = () => {
      const cap = gCap(), years = gYears(), rate = gRate() / 100;
      const real = cap / Math.pow(1 + rate, years);
      const loss = cap - real;
      document.getElementById("infLoss").textContent = "\u2212" + fmtEUR(loss);
      document.getElementById("infNom").textContent = fmtEUR(cap);
      document.getElementById("infReal").textContent = fmtEUR(real);
      document.getElementById("infNomBar").style.width = "100%";
      document.getElementById("infRealBar").style.width = (cap > 0 ? (real / cap) * 100 : 0) + "%";
    };
    gCap = bindControl("infCap", update);
    gYears = bindControl("infYears", update);
    gRate = bindControl("infRate", update);
    update();
  }

  /* ---------- Calcolatore 2 (quando intervengo): interesse composto / PAC ---------- */
  if (document.getElementById("pacInit")) {
    let gInit, gMonthly, gYears, gRate;
    const chartEl = document.getElementById("pacChart");

    // Valore futuro a fine anno k (capitalizzazione mensile, versamenti a fine mese)
    const fvAtYear = (init, m, im, k) => {
      const n = 12 * k;
      if (im === 0) return init + m * n;
      const f = Math.pow(1 + im, n);
      return init * f + m * ((f - 1) / im);
    };

    const fmtShort = (n) => {
      if (n >= 1e6) return (n / 1e6).toLocaleString("it-IT", { maximumFractionDigits: 1 }) + " mln \u20AC";
      if (n >= 1e3) return Math.round(n / 1e3).toLocaleString("it-IT") + ".000 \u20AC";
      return Math.round(n) + " \u20AC";
    };

    const drawChart = (init, m, im, years, finalV) => {
      const W = 640, H = 320, padL = 78, padR = 12, padT = 16, padB = 34;
      const plotW = W - padL - padR, plotH = H - padT - padB;
      const yMax = Math.max(finalV, 1) * 1.05;
      const yScale = (v) => padT + plotH - (v / yMax) * plotH;
      const n = years;
      const slot = plotW / n;
      const bw = Math.max(Math.min(slot * 0.62, 46), 3);
      let bars = "", labels = "", grid = "";

      for (let g = 0; g <= 4; g++) {
        const v = (yMax / 4) * g;
        const y = yScale(v);
        grid += `<line x1="${padL}" y1="${y}" x2="${W - padR}" y2="${y}" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>`
              + `<text x="${padL - 10}" y="${y + 4}" text-anchor="end" font-size="11" fill="rgba(169,167,159,0.8)">${fmtShort(v)}</text>`;
      }

      const labelStep = years > 30 ? 10 : years > 12 ? 5 : years > 6 ? 2 : 1;
      for (let k = 1; k <= n; k++) {
        const fv = fvAtYear(init, m, im, k);
        const contrib = m * 12 * k;
        const interest = Math.max(fv - init - contrib, 0);
        const x = padL + slot * (k - 1) + (slot - bw) / 2;
        const yTop = yScale(init + contrib + interest);
        const yInit = yScale(init);
        const yContrib = yScale(init + contrib);
        bars += `<rect x="${x}" y="${yInit}" width="${bw}" height="${plotH + padT - yInit}" rx="2" fill="#8B877F"/>`
              + `<rect x="${x}" y="${yContrib}" width="${bw}" height="${yInit - yContrib}" rx="2" fill="#F2EFE9"/>`
              + `<rect x="${x}" y="${yTop}" width="${bw}" height="${yContrib - yTop}" rx="2" fill="#C8A96E"/>`;
        if (k % labelStep === 0 || k === n) {
          labels += `<text x="${x + bw / 2}" y="${H - 12}" text-anchor="middle" font-size="11" fill="rgba(169,167,159,0.8)">${k}a</text>`;
        }
      }
      chartEl.innerHTML = `<svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Crescita del capitale anno per anno">${grid}${bars}${labels}</svg>`;
    };

    const update = () => {
      const init = gInit(), m = gMonthly(), years = Math.max(Math.round(gYears()), 1), rate = gRate() / 100;
      const im = rate / 12;
      const finalV = fvAtYear(init, m, im, years);
      const paid = init + m * 12 * years;
      document.getElementById("pacFinal").textContent = fmtEUR(finalV);
      document.getElementById("pacPaid").textContent = "di cui versati: " + fmtEUR(paid);
      drawChart(init, m, im, years, finalV);
    };
    gInit = bindControl("pacInit", update);
    gMonthly = bindControl("pacMonthly", update);
    gYears = bindControl("pacYears", update);
    gRate = bindControl("pacRate", update);
    update();
  }

  /* ---------- Calcolatore 3 (imprese): liquidita' eccedente, tre scenari ---------- */
  if (document.getElementById("bizCap")) {
    let gCap, gYears, gInf, gRet;
    const update = () => {
      const cap = gCap(), years = gYears(), inf = gInf() / 100, ret = gRet() / 100;
      const realStill = cap / Math.pow(1 + inf, years);
      const realInvest = cap * Math.pow((1 + ret) / (1 + inf), years);
      const diff = realInvest - realStill;
      const maxV = Math.max(cap, realInvest);
      document.getElementById("bizNom").textContent = fmtEUR(cap);
      document.getElementById("bizStill").textContent = fmtEUR(realStill);
      document.getElementById("bizInvest").textContent = fmtEUR(realInvest);
      document.getElementById("bizDiff").textContent = (diff >= 0 ? "+" : "\u2212") + fmtEUR(Math.abs(diff));
      document.getElementById("bizNomBar").style.width = (cap / maxV) * 100 + "%";
      document.getElementById("bizStillBar").style.width = (realStill / maxV) * 100 + "%";
      document.getElementById("bizInvestBar").style.width = (realInvest / maxV) * 100 + "%";
    };
    gCap = bindControl("bizCap", update);
    gYears = bindControl("bizYears", update);
    gInf = bindControl("bizInf", update);
    gRet = bindControl("bizRet", update);
    update();
  }

  /* ---------- 6. Anno footer ---------- */
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
