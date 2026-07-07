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

  /* ---------- 6. Anno footer ---------- */
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
