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

  const setMenu = (open) => {
    navLinks.classList.toggle("is-open", open);
    navToggle.classList.toggle("is-open", open);
    nav.classList.toggle("menu-open", open);
    document.body.classList.toggle("menu-open", open);
    navToggle.setAttribute("aria-expanded", String(open));
    navToggle.setAttribute("aria-label", open ? "Chiudi menu" : "Apri menu");
  };

  if (navToggle) {
    navToggle.addEventListener("click", () => setMenu(!navLinks.classList.contains("is-open")));
    navLinks.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setMenu(false)));
    // Chiusura con ESC (tastiere fisiche / accessibilità)
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && navLinks.classList.contains("is-open")) setMenu(false);
    });
    // Se si passa a viewport desktop con il menu aperto, ripulisco lo stato
    window.addEventListener("resize", () => {
      if (window.innerWidth > 720 && navLinks.classList.contains("is-open")) setMenu(false);
    });
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

  /* ==========================================================================
     3. HERO: "La Rotta" — dal patrimonio frammentato a una direzione consapevole
     Narrazione automatica (~5s): punti dispersi -> traiettorie che si disegnano
     in sequenza -> equilibrio, con impulso dorato lungo la rotta e CTA illuminata.
     Lo scroll dentro la hero accelera la convergenza (nessun blocco dello scroll);
     il mouse esercita solo una lieve attrazione magnetica.
     ========================================================================== */
  const canvas = document.getElementById("heroCanvas");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (canvas) {
    const ctx = canvas.getContext("2d");
    const hero = canvas.closest(".hero");
    const DPR = Math.min(window.devicePixelRatio || 1, 2);
    const DURATION = 5200;
    const mouse = { x: -9999, y: -9999 };
    let w, h, dust, route, raf, start = null, scrollBoost = 0;

    const ease = (t) => 1 - Math.pow(1 - t, 3);

    // Rotta: curva di Bezier che converge verso l'area della CTA
    const curvePoint = (t) => {
      const endX = w < 720 ? 0.44 : 0.34;
      const P0 = { x: w * 0.90, y: h * 0.16 };
      const P1 = { x: w * 0.74, y: h * 0.64 };
      const P2 = { x: w * 0.54, y: h * 0.28 };
      const P3 = { x: w * endX, y: h * 0.76 };
      const u = 1 - t;
      return {
        x: u * u * u * P0.x + 3 * u * u * t * P1.x + 3 * u * t * t * P2.x + t * t * t * P3.x,
        y: u * u * u * P0.y + 3 * u * u * t * P1.y + 3 * u * t * t * P2.y + t * t * t * P3.y,
      };
    };

    const build = () => {
      w = canvas.offsetWidth;
      h = canvas.offsetHeight;
      canvas.width = w * DPR;
      canvas.height = h * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);

      const dustCount = Math.min(Math.floor((w * h) / 26000), 55);
      dust = Array.from({ length: dustCount }, () => ({
        x: Math.random() * w, y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.08, vy: (Math.random() - 0.5) * 0.08,
        r: Math.random() * 1.3 + 0.5,
        a: Math.random() * 0.22 + 0.14,
      }));

      const K = 9;
      route = Array.from({ length: K }, (_, i) => {
        const target = curvePoint(i / (K - 1));
        return {
          sx: Math.random() * w, sy: Math.random() * h,
          tx: target.x, ty: target.y,
          delay: 0.14 + (i / (K - 1)) * 0.34, // i nodi si ordinano in sequenza lungo la rotta
        };
      });
    };

    // Attrazione magnetica lieve verso il cursore (pochi pixel, mai vistosa)
    const attract = (px, py, maxPull) => {
      const dx = mouse.x - px, dy = mouse.y - py;
      const d = Math.hypot(dx, dy);
      const R = 240;
      if (d > R || d === 0) return { x: px, y: py };
      const f = (1 - d / R) * maxPull;
      return { x: px + (dx / d) * f, y: py + (dy / d) * f };
    };

    const render = (p, now) => {
      ctx.clearRect(0, 0, w, h);

      // Primo momento: polvere dispersa, quasi immobile
      for (const d of dust) {
        d.x += d.vx; d.y += d.vy;
        if (d.x < 0 || d.x > w) d.vx *= -1;
        if (d.y < 0 || d.y > h) d.vy *= -1;
        const pos = attract(d.x, d.y, 6);
        ctx.fillStyle = "rgba(242,239,233," + d.a + ")";
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, d.r, 0, Math.PI * 2);
        ctx.fill();
      }

      // Nodi della rotta: dai punti dispersi alle posizioni ordinate
      const pts = route.map((n) => {
        const lp = Math.min(Math.max((p - n.delay) / 0.4, 0), 1);
        const e = ease(lp);
        const base = { x: n.sx + (n.tx - n.sx) * e, y: n.sy + (n.ty - n.sy) * e };
        const q = attract(base.x, base.y, 3);
        return { x: q.x, y: q.y, settled: lp };
      });

      // Le traiettorie emergono: ogni segmento si disegna in sequenza
      for (let i = 0; i < pts.length - 1; i++) {
        const segStart = 0.32 + (i / (pts.length - 1)) * 0.40;
        const sp = Math.min(Math.max((p - segStart) / 0.14, 0), 1);
        if (sp <= 0) continue;
        const a = pts[i], b = pts[i + 1];
        const alpha = (0.16 + 0.30 * Math.min(p * 1.2, 1)) * sp;
        ctx.strokeStyle = "rgba(200,169,110," + alpha + ")";
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(a.x + (b.x - a.x) * sp, a.y + (b.y - a.y) * sp);
        ctx.stroke();
      }

      // Nodi
      for (const q of pts) {
        ctx.fillStyle = "rgba(242,239,233," + (0.30 + 0.50 * q.settled) + ")";
        ctx.shadowColor = "rgba(200,169,110,0.8)";
        ctx.shadowBlur = 3 + 6 * q.settled;
        ctx.beginPath();
        ctx.arc(q.x, q.y, 1.6 + 1.3 * q.settled, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      // Equilibrio: un impulso di luce percorre la rotta e la CTA si accende
      if (p > 0.92) {
        if (now !== null) {
          const t = (now / 2600) % 1;
          const gp = curvePoint(t);
          const grad = ctx.createRadialGradient(gp.x, gp.y, 0, gp.x, gp.y, 26);
          grad.addColorStop(0, "rgba(227,201,143,0.45)");
          grad.addColorStop(1, "rgba(227,201,143,0)");
          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.arc(gp.x, gp.y, 26, 0, Math.PI * 2);
          ctx.fill();
        }
        hero.classList.add("is-lit");
      }
    };

    const draw = (now) => {
      if (start === null) start = now;
      const p = Math.min(ease(Math.min((now - start) / DURATION, 1)) + scrollBoost, 1);
      render(p, now);
      raf = requestAnimationFrame(draw);
    };

    hero.addEventListener("pointermove", (e) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });
    hero.addEventListener("pointerleave", () => { mouse.x = -9999; mouse.y = -9999; });

    build();

    if (reduceMotion) {
      // Accessibilita': stato finale statico, senza animazione
      render(1, null);
    } else {
      // Lo scroll dentro la hero accelera la convergenza (senza mai bloccarla)
      window.addEventListener("scroll", () => {
        scrollBoost = Math.min(window.scrollY / (h * 0.9), 1) * 0.18;
      }, { passive: true });

      const heroObserver = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) raf = requestAnimationFrame(draw);
        else cancelAnimationFrame(raf);
      });
      heroObserver.observe(canvas);
      window.addEventListener("resize", build);
    }
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
