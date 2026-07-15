#!/usr/bin/env python3
"""Genera le pagine del sito da template condivisi (header/footer identici ovunque)."""

LI_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4V24h-4V8zm7.5 0h3.8v2.2h.05c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.78 2.65 4.78 6.1V24h-4v-8.5c0-2-.04-4.6-2.8-4.6-2.8 0-3.23 2.2-3.23 4.45V24H8V8z"/></svg>'
MAIL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.24-8 5-8-5V6.1l8 5 8-5v2.14z"/></svg>'
TEL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.61 21 3 13.39 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.24.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2z"/></svg>'

LINKEDIN_URL = "https://www.linkedin.com/in/matteo-notario-691424167/"
EMAIL = "matteo.notario@pfafineco.it"
TEL = "+39 329 877 6611"
TEL_HREF = "+393298776611"

def head(title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Matteo Notario">
  <link rel="canonical" href="https://www.tuodominio.it/{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://www.tuodominio.it/{canonical}">
  <meta property="og:image" content="https://www.tuodominio.it/img/og-cover.jpg">
  <meta property="og:locale" content="it_IT">
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
'''

NAV = f'''  <header class="nav" id="nav">
    <div class="nav__inner">
      <a href="index.html" class="nav__logo" aria-label="Matteo Notario — Home">
        <img src="img/logo-bianco.png" alt="Matteo Notario — Financial Advisor Fineco">
      </a>
      <nav class="nav__links" id="navLinks" aria-label="Navigazione principale">
        <a href="index.html">Home</a>
        <a href="chi-sono.html">Chi sono</a>
        <a href="metodo.html">Metodo</a>
        <a href="quando-intervengo.html">Quando intervengo</a>
        <a href="per-le-imprese.html">Per le imprese</a>
        <a href="articoli.html">Articoli</a>
      </nav>
      <a href="contatti.html" class="btn btn--nav">Contattami</a>
      <button class="nav__toggle" id="navToggle" aria-label="Apri menu" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>
  </header>
'''

FOOTER = f'''  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <img src="img/logo-bianco.png" alt="Matteo Notario — Financial Advisor Fineco">
        <p>Consulenza patrimoniale con metodo strategico,<br>per persone e imprese nei momenti che contano.</p>
      </div>
      <div class="footer__col">
        <h4>Contatti</h4>
        <a href="mailto:{EMAIL}">{MAIL_ICON}{EMAIL}</a>
        <a href="tel:{TEL_HREF}">{TEL_ICON}{TEL}</a>
        <a href="{LINKEDIN_URL}" target="_blank" rel="noopener">{LI_ICON}LinkedIn</a>
      </div>
      <div class="footer__col">
        <h4>Esplora</h4>
        <a href="metodo.html">Il metodo</a>
        <a href="quando-intervengo.html">Quando intervengo</a>
        <a href="articoli.html">Articoli</a>
        <a href="privacy.html">Privacy &amp; Cookie</a>
      </div>
    </div>
    <div class="container footer__legal">
      <p>Matteo Notario — Consulente Finanziario abilitato all'offerta fuori sede per FinecoBank S.p.A. Iscritto all'Albo unico dei Consulenti Finanziari con delibera n. 2662 del 28/01/2025. P.IVA 13202740018.</p>
      <p>Le informazioni contenute nel presente sito internet sono curate dal consulente di riferimento, come Consulente Finanziario abilitato all'offerta fuori sede per FinecoBank S.p.A., e soggetto autorizzato e vigilato da Consob. Queste informazioni non costituiscono in alcun modo raccomandazioni personalizzate rispetto alle caratteristiche del singolo lettore e potrebbero non essere adeguate rispetto alle sue conoscenze, alle sue esperienze, alla sua situazione finanziaria ed ai suoi obiettivi di investimento. Le informazioni contenute nel presente sito internet sono da intendersi a scopo puramente informativo. FinecoBank S.p.A. non si assume alcuna responsabilità in merito alla correttezza, alla completezza e alla veridicità delle informazioni fornite.</p>
      <p>© <span id="year"></span> Matteo Notario. Tutti i diritti riservati.</p>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
'''

def cta_band(title, sub, label="Prenota una conversazione"):
    return f'''    <section class="cta-band">
      <div class="container">
        <h2 class="reveal">{title}</h2>
        <p class="reveal">{sub}</p>
        <a href="contatti.html" class="btn btn--primary reveal">{label}</a>
      </div>
    </section>
'''

pages = {}

# ============================================================ HOMEPAGE
pages["index.html"] = head(
    "Matteo Notario — Consulenza Patrimoniale Strategica",
    "Non ti aiuto a scegliere prodotti finanziari: ti aiuto a prendere decisioni migliori quando il tuo patrimonio cambia. Consulenza con metodo strategico per persone e imprese.",
    ""
) + NAV + f'''
  <main>
    <section class="hero">
      <div class="hero__aurora" aria-hidden="true"><span></span><span></span><span></span></div>
      <canvas id="heroCanvas" class="hero__canvas" aria-hidden="true"></canvas>
      <div class="hero__content container">
        <p class="hero__eyebrow reveal">Matteo Notario — Consulenza patrimoniale strategica</p>
        <h1 class="hero__title">
          <span class="reveal d1">Non ti aiuto a scegliere</span>
          <span class="reveal d2">prodotti finanziari.</span>
          <span class="hero__title-accent reveal d3">Ti aiuto a prendere decisioni consapevoli, quando il tuo patrimonio cambia.</span>
        </h1>
        <p class="hero__sub reveal d4">
          Un'eredità, la vendita di un'azienda o di un immobile, un progetto di vita da realizzare:
          sono momenti in cui il patrimonio diventa decisione. Ti aiuto ad affrontarli con lucidità,
          metodo e una visione d'insieme maturata nelle scelte patrimoniali più importanti.
        </p>
        <div class="hero__cta reveal d5">
          <a href="contatti.html" class="btn btn--primary">Richiedi una prima analisi</a>
          <a href="metodo.html" class="btn btn--ghost">Scopri il metodo</a>
        </div>
      </div>
      <div class="hero__scroll" aria-hidden="true"><span></span></div>
    </section>

    <section class="pain section">
      <div class="container">
        <p class="section__eyebrow reveal">Una domanda scomoda</p>
        <h2 class="section__title reveal">Il tuo patrimonio segue un progetto<br>o segue l'inerzia?</h2>
        <p class="section__intro reveal">
          La maggior parte dei patrimoni non viene gestita: procede senza una direzione.
          Questi sono i segnali che incontro più spesso.
        </p>
        <div class="pain__grid">
          <article class="pain__card reveal">
            <span class="pain__num">01</span>
            <h3>Decisioni prese per abitudine</h3>
            <p>La banca "di famiglia", i prodotti sottoscritti anni fa e mai più rivisti. Nessuna azienda seria lavorerebbe così — nessun patrimonio dovrebbe.</p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">02</span>
            <h3>Capitale senza un progetto</h3>
            <p>Investimenti accumulati nel tempo, senza una strategia che risponda alla domanda fondamentale: <em>a cosa serve questo patrimonio, e quando?</em></p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">03</span>
            <h3>Costi invisibili</h3>
            <p>Commissioni, retrocessioni, prodotti inefficienti: ogni anno erodono silenziosamente i rendimenti. Su dieci, vent'anni, la differenza è enorme.</p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">04</span>
            <h3>Consigli senza una regia</h3>
            <p>Tanti interlocutori — banca, commercialista, assicuratore — ma nessuno che guardi il quadro d'insieme e risponda di una strategia complessiva.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="calc section" id="quanto-costa-non-decidere">
      <div class="container">
        <p class="section__eyebrow reveal">Prova con i tuoi numeri</p>
        <h2 class="section__title reveal">Quanto costa <span class="title-accent">non decidere?</span></h2>
        <p class="section__intro reveal">
          La liquidità ferma sul conto sembra al sicuro. In realtà l'inflazione ne erode
          il potere d'acquisto ogni anno, in silenzio. Muovi i cursori e guarda l'effetto sui tuoi numeri.
        </p>
        <div class="calc__panel reveal">
          <div class="calc__controls">
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="infCapNum">Liquidità ferma sul conto</label>
                <span class="calc__value"><input type="number" id="infCapNum" value="250000" min="0"><span class="calc__unit">€</span></span>
              </div>
              <input type="range" class="calc__range" id="infCap" min="10000" max="20000000" step="10000" value="250000" aria-label="Liquidità ferma sul conto">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="infYearsNum">Orizzonte temporale</label>
                <span class="calc__value"><input type="number" id="infYearsNum" value="10" min="0"><span class="calc__unit">anni</span></span>
              </div>
              <input type="range" class="calc__range" id="infYears" min="1" max="30" step="1" value="10" aria-label="Orizzonte temporale">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="infRateNum">Inflazione media annua</label>
                <span class="calc__value"><input type="number" id="infRateNum" value="2" min="0"><span class="calc__unit">%</span></span>
              </div>
              <input type="range" class="calc__range" id="infRate" min="0" max="15" step="0.5" value="2" aria-label="Inflazione media annua">
            </div>
          </div>
          <div class="calc__results">
            <div class="calc__headline">
              <span class="calc__headline-label">Potere d'acquisto perso</span>
              <span class="calc__headline-value is-neg" id="infLoss">− 0 €</span>
            </div>
            <div>
              <div class="calc__bar-label"><span>Cifra sul conto (nominale)</span><strong id="infNom">—</strong></div>
              <div class="calc__bar calc__bar--nominal"><span id="infNomBar"></span></div>
            </div>
            <div>
              <div class="calc__bar-label"><span>Cosa potrai comprarci davvero</span><strong id="infReal">—</strong></div>
              <div class="calc__bar calc__bar--real"><span id="infRealBar"></span></div>
            </div>
            <p class="calc__note">Simulazione a scopo puramente illustrativo ed educativo, al lordo di costi e fiscalità: non costituisce consulenza personalizzata, offerta o promessa di rendimento. L'inflazione futura non è nota in anticipo.</p>
          </div>
        </div>
        <div class="calc__cta reveal">
          <a href="contatti.html" class="btn btn--primary">Prenota un primo confronto</a>
        </div>
      </div>
    </section>

    <section class="statement section">
      <div class="container">
        <blockquote class="statement__quote reveal">
          Non sono <em>"quello degli investimenti"</em>.<br>
          Sono il professionista che entra in gioco nei
          <span class="statement__accent">momenti di transizione economica</span>
          delle persone e delle imprese.
        </blockquote>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section__eyebrow reveal">Il metodo</p>
        <h2 class="section__title reveal">Decidere con metodo,<br>non per abitudine.</h2>
        <p class="section__intro reveal">
          Per anni ho lavorato come consulente strategico per grandi multinazionali.
          Il mio obiettivo è portare quel metodo nella consulenza finanziaria, attraverso 4 step.
        </p>
        <div class="method__steps">
          <article class="method__step reveal" data-n="01">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 01</div>
            <h3>Diagnosi</h3>
            <p>Capire dove sei: patrimonio, obiettivi, orizzonte, fiscalità, rischi.</p>
          </article>
          <article class="method__step reveal" data-n="02">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 02</div>
            <h3>Strategia</h3>
            <p>Un progetto scritto, con priorità, alternative e scenari.</p>
          </article>
          <article class="method__step reveal" data-n="03">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 03</div>
            <h3>Esecuzione</h3>
            <p>Strumenti efficienti e trasparenti, al servizio del progetto.</p>
          </article>
          <article class="method__step reveal" data-n="04">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 04</div>
            <h3>Governance</h3>
            <p>Monitoraggio continuo e revisioni a ogni cambio di scenario.</p>
          </article>
        </div>
        <div class="teaser__link reveal">
          <a href="metodo.html" class="arrow-link">Approfondisci il metodo e le differenze</a>
        </div>
      </div>
    </section>

    <section class="cases section">
      <div class="container">
        <p class="section__eyebrow reveal">Quando intervengo</p>
        <h2 class="section__title reveal">I momenti in cui una decisione<br>sbagliata costa più cara.</h2>
        <div class="cases__grid">
          <article class="cases__card reveal">
            <h3>Vuoi pianificare il tuo patrimonio</h3>
            <p>Dalla protezione della famiglia alla pensione, dal fisco al passaggio generazionale: un progetto unico, non prodotti scollegati.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Vuoi rendimenti — con metodo</h3>
            <p>Non promesse di performance: portafogli efficienti, costi sotto controllo e disciplina in ogni fase di mercato.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Hai ricevuto un'eredità</h3>
            <p>Un capitale importante e la responsabilità di non disperderlo: trasformiamolo in un progetto, non in scelte improvvisate.</p>
          </article>
        </div>
        <div class="teaser__link reveal">
          <a href="quando-intervengo.html" class="arrow-link">Vedi tutte le situazioni in cui posso aiutarti</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section__eyebrow reveal">Per le imprese</p>
        <h2 class="section__title reveal">Finanza, previdenza, formazione:<br>tre leve, un unico interlocutore.</h2>
        <p class="section__intro reveal">
          Supporto imprenditori e PMI su tre fronti: la pianificazione finanziaria dell'impresa
          — liquidità, protezione, continuità —, la previdenza aziendale, dal TFM degli
          amministratori al TFR dei dipendenti, e la formazione finanziaria in azienda.
        </p>
        <div class="teaser__link reveal">
          <a href="per-le-imprese.html" class="arrow-link">Scopri i servizi per le imprese</a>
        </div>
      </div>
    </section>

{cta_band("Una conversazione, nessun impegno.",
          "30 minuti per capire la tua situazione e dirti — con onestà — se e come posso esserti utile. Se non sono la persona giusta, te lo dico.")}
  </main>
''' + FOOTER

# ============================================================ CHI SONO
pages["chi-sono.html"] = head(
    "Chi sono — Matteo Notario, Consulente Finanziario",
    "Ex consulente strategico per grandi multinazionali, oggi consulente finanziario. Porto nel patrimonio delle persone il rigore delle decisioni aziendali.",
    "chi-sono.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Chi sono</p>
        <h1 class="reveal d1">Dalla strategia d'impresa<br>alla strategia patrimoniale.</h1>
        <p class="reveal d2">
          Aiuto persone, famiglie e imprenditori a prendere decisioni patrimoniali con lo stesso
          rigore con cui si affrontano le scelte strategiche di un'azienda.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section-lead reveal">
          Dalla mia esperienza nasce il mio modo di lavorare: poche promesse,
          molta chiarezza e un metodo documentato.
        </p>
      </div>
      <div class="container about__inner">
        <div class="about__photo reveal">
          <div class="about__photo-frame">
            <img src="img/matteo-notario.jpg" alt="Matteo Notario, consulente finanziario">
          </div>
          <p class="about__photo-caption">Matteo Notario — Financial Advisor, Fineco</p>
        </div>
        <div class="about__text">
          <p class="reveal">
            Per anni ho lavorato come <strong>consulente strategico per grandi multinazionali</strong>,
            affiancando il management in decisioni complesse: digitalizzazione, investimenti,
            riorganizzazioni e crescita. In quel percorso ho imparato una cosa essenziale:
            <strong>non sempre le decisioni migliori nascono dall'istinto, ma da un metodo</strong>.
          </p>
          <p class="reveal">
            Oggi porto quello stesso metodo nella gestione del patrimonio di persone, famiglie
            e imprese, aiutando chi affronta passaggi patrimoniali importanti a scegliere
            con lucidità, ordine e visione d'insieme.
          </p>
          <p class="reveal">
            Lavoro anche con chi non sta vivendo una transizione particolare, ma sente che
            è arrivato il momento di smettere di gestire il proprio patrimonio per inerzia
            e vuole iniziare a dargli una direzione.
          </p>
          <div class="about__values">
            <div class="reveal">
              <strong>Un metodo, non un prodotto</strong>
              <span>Ogni raccomandazione nasce da un'analisi documentata dei tuoi obiettivi, mai da un catalogo.</span>
            </div>
            <div class="reveal">
              <strong>Trasparenza e chiarezza</strong>
              <span>Lavoro a parcella, con un compenso definito in anticipo e indipendente dagli strumenti consigliati. Ogni costo è esplicito, ogni scelta spiegata.</span>
            </div>
            <div class="reveal">
              <strong>Presenza nei momenti difficili</strong>
              <span>Il mio lavoro vale di più quando i mercati fanno paura: è lì che la disciplina protegge il progetto.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="statement" style="padding: 5.5rem 0;">
      <div class="container">
        <blockquote class="statement__quote reveal" style="max-width: 32ch; font-size: clamp(1.35rem, 2.6vw, 2rem);">
          Se stai affrontando una decisione patrimoniale importante, possiamo partire da una
          <span class="statement__accent">conversazione semplice</span>:
          capire dove sei, cosa vuoi proteggere e quali scelte hai davanti.
        </blockquote>
      </div>
    </section>

{cta_band("Vuoi capire se posso esserti utile?",
          "Prima di parlare di soluzioni, ascolto la tua situazione. La prima conversazione serve a capire dove sei, quali decisioni hai davanti e se posso esserti utile.")}
  </main>
''' + FOOTER

# ============================================================ METODO
pages["metodo.html"] = head(
    "Il Metodo — Matteo Notario, Consulenza Patrimoniale Strategica",
    "Quattro fasi — diagnosi, strategia, esecuzione, governance — per decidere con metodo, non per abitudine. Il rigore della consulenza strategica applicato al patrimonio.",
    "metodo.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Il metodo</p>
        <h1 class="reveal d1">Decidere con metodo,<br>non per abitudine.</h1>
        <p class="reveal d2">
          Un metodo in 4 fasi per trasformare patrimonio, obiettivi e decisioni complesse
          in una strategia chiara, documentata e monitorata nel tempo.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section-lead reveal">
          Dal primo confronto al monitoraggio nel tempo: ogni fase ha un obiettivo preciso,
          un metodo di lavoro e un risultato concreto.
        </p>
        <div class="method__steps">
          <article class="method__step reveal" data-n="01">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 01</div>
            <h3>Diagnosi</h3>
            <p>Mettiamo ordine nella situazione: patrimonio, obiettivi, tempi, fiscalità, rischi e priorità. Prima di proporre soluzioni, capisco davvero dove sei e dove vuoi arrivare.</p>
          </article>
          <article class="method__step reveal" data-n="02">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 02</div>
            <h3>Strategia</h3>
            <p>Costruiamo un progetto patrimoniale, con priorità, alternative e scenari. Ogni scelta deve avere una motivazione chiara, non essere figlia dell'abitudine.</p>
          </article>
          <article class="method__step reveal" data-n="03">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 03</div>
            <h3>Esecuzione</h3>
            <p>Traduciamo la strategia in azioni concrete, scegliendo strumenti coerenti, efficienti e trasparenti nei costi. Gli strumenti servono il progetto, non il contrario.</p>
          </article>
          <article class="method__step reveal" data-n="04">
            <span class="method__node" aria-hidden="true"></span>
            <div class="method__phase">Fase 04</div>
            <h3>Governance</h3>
            <p>Monitoriamo il percorso nel tempo, con revisioni periodiche e presenza nei momenti difficili. È lì che il metodo smette di essere teoria e diventa valore.</p>
          </article>
        </div>

        <div class="offer reveal">
          <div class="offer__text">
            <span class="offer__tag">Gratuita e senza impegno</span>
            <h3>Hai già un portafoglio? Mettiamolo alla prova.</h3>
            <p>Se i tuoi investimenti sono seguiti da altri intermediari, posso applicare la Fase 01 del metodo al tuo portafoglio attuale: una diagnosi chiara su costi, rischi e coerenza con i tuoi obiettivi, restituita per iscritto.</p>
          </div>
          <a href="contatti.html" class="btn btn--primary">Prenotala gratuitamente</a>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top: 0;">
      <div class="container">
        <p class="section__eyebrow reveal">La differenza</p>
        <h2 class="section__title reveal">Due modi opposti di intendere la consulenza finanziaria.</h2>
        <div class="compare__table reveal" role="table" aria-label="Confronto tra approccio tradizionale e approccio strategico">
          <div class="compare__row compare__row--head" role="row">
            <div role="columnheader">Approccio tradizionale</div>
            <div role="columnheader" class="compare__ours">Approccio strategico</div>
          </div>
          <div class="compare__row" role="row">
            <div role="cell" data-label="Approccio tradizionale">Parte dal prodotto da proporre</div>
            <div role="cell" class="compare__ours" data-label="Approccio strategico"><span class="compare__arrow" aria-hidden="true">→</span>Parte dall'analisi dei tuoi obiettivi</div>
          </div>
          <div class="compare__row" role="row">
            <div role="cell" data-label="Approccio tradizionale">Costi poco visibili e frammentati</div>
            <div role="cell" class="compare__ours" data-label="Approccio strategico"><span class="compare__arrow" aria-hidden="true">→</span>Costi dichiarati e documentati</div>
          </div>
          <div class="compare__row" role="row">
            <div role="cell" data-label="Approccio tradizionale">Portafoglio come somma di prodotti</div>
            <div role="cell" class="compare__ours" data-label="Approccio strategico"><span class="compare__arrow" aria-hidden="true">→</span>Patrimonio come progetto unitario</div>
          </div>
        </div>
      </div>
    </section>

{cta_band("Il metodo funziona se parte dalla tua situazione.",
          "Raccontamela in una prima conversazione conoscitiva: 30 minuti, senza impegno.",
          "Prenota un primo confronto")}
  </main>
''' + FOOTER

# ============================================================ QUANDO INTERVENGO
pages["quando-intervengo.html"] = head(
    "Quando intervengo — Matteo Notario, Consulenza Patrimoniale",
    "Eredità, vendita d'azienda, operazioni immobiliari, pianificazione patrimoniale: i momenti di transizione economica in cui una decisione sbagliata costa più cara.",
    "quando-intervengo.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Quando intervengo</p>
        <h1 class="reveal d1">I momenti in cui una decisione<br>sbagliata costa più cara.</h1>
        <p class="reveal d2">
          Quelli che seguono sono alcuni esempi delle situazioni in cui posso darti supporto —
          i più frequenti, non gli unici. Se la tua situazione non è tra queste,
          parliamone: ogni transizione patrimoniale merita un'analisi dedicata.
        </p>
      </div>
    </section>

    <section class="cases section">
      <div class="container">
        <p class="section-lead reveal">
          Alcune decisioni patrimoniali non sono solo finanziarie: arrivano quando cambia
          una fase della vita, dell'impresa o della famiglia. In quei momenti serve metodo,
          ma anche una guida capace di mettere ordine.
        </p>
        <div class="cases__grid">
          <article class="cases__card reveal">
            <h3>Vuoi pianificare il tuo patrimonio</h3>
            <p>Non basta scegliere prodotti: serve una regia. Obiettivi, protezione familiare, pensione, fiscalità e passaggio generazionale devono stare dentro un unico disegno.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Vuoi rendimenti — con metodo</h3>
            <p>Il rendimento non si insegue. Si costruisce con portafogli efficienti, costi sotto controllo, disciplina e coerenza con i tuoi obiettivi.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Hai ricevuto un'eredità</h3>
            <p>Un capitale improvviso può diventare una risorsa o una fonte di decisioni affrettate. Ti aiuto a trasformarlo in un progetto ordinato.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Hai venduto la tua azienda</h3>
            <p>Dopo anni di lavoro, la liquidità non va semplicemente “investita”. Va protetta, organizzata e collegata alla tua nuova fase personale e patrimoniale.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Hai concluso un'operazione immobiliare</h3>
            <p>Una vendita importante cambia equilibri, fiscalità e prospettive. Serve una strategia che tenga insieme rendimento, protezione e liquidità.</p>
          </article>
          <article class="cases__card reveal">
            <h3>Un punto di riferimento in ogni fase di mercato</h3>
            <p>Nei momenti difficili il valore non è prevedere tutto, ma avere una rotta, un metodo e qualcuno che non sparisca quando aumenta il rumore.</p>
          </article>
        </div>
        <p class="section__note reveal">
          La tua situazione è diversa da queste? È normale: ogni patrimonio ha una storia propria.
          <a href="contatti.html" style="color: var(--brass-hi);">Raccontami la tua</a>.
        </p>
      </div>
    </section>

    <section class="calc section" id="il-tempo-lavora-per-te">
      <div class="container">
        <p class="section__eyebrow reveal">Prova con i tuoi numeri</p>
        <h2 class="section__title reveal">Il tempo lavora per te. <span class="title-accent">Guarda quanto.</span></h2>
        <p class="section__intro reveal">
          Un piano di accumulo trasforma un versamento mensile sostenibile in capitale,
          sfruttando l'interesse composto. Muovi i cursori: il grafico si aggiorna in tempo reale.
        </p>
        <div class="calc__panel reveal">
          <div class="calc__controls">
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="pacInitNum">Capitale iniziale</label>
                <span class="calc__value"><input type="number" id="pacInitNum" value="10000" min="0"><span class="calc__unit">€</span></span>
              </div>
              <input type="range" class="calc__range" id="pacInit" min="0" max="1000000" step="1000" value="10000" aria-label="Capitale iniziale">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="pacMonthlyNum">Versamento mensile</label>
                <span class="calc__value"><input type="number" id="pacMonthlyNum" value="300" min="0"><span class="calc__unit">€</span></span>
              </div>
              <input type="range" class="calc__range" id="pacMonthly" min="50" max="250000" step="50" value="300" aria-label="Versamento mensile">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="pacYearsNum">Durata del piano</label>
                <span class="calc__value"><input type="number" id="pacYearsNum" value="20" min="0"><span class="calc__unit">anni</span></span>
              </div>
              <input type="range" class="calc__range" id="pacYears" min="1" max="50" step="1" value="20" aria-label="Durata del piano">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="pacRateNum">Ipotesi di rendimento medio annuo</label>
                <span class="calc__value"><input type="number" id="pacRateNum" value="4" min="0"><span class="calc__unit">%</span></span>
              </div>
              <input type="range" class="calc__range" id="pacRate" min="0" max="15" step="0.5" value="4" aria-label="Ipotesi di rendimento medio annuo">
            </div>
            <div class="calc__headline">
              <span class="calc__headline-label">Capitale stimato a scadenza</span>
              <span class="calc__headline-value is-pos" id="pacFinal">0 €</span>
              <span class="calc__headline-sub" id="pacPaid">di cui versati: 0 €</span>
            </div>
          </div>
          <div class="calc__results">
            <div class="calc__chart" id="pacChart" aria-live="polite"></div>
            <div class="calc__legend">
              <span><i style="background:#8B877F"></i> Capitale iniziale</span>
              <span><i style="background:#F2EFE9"></i> Versamenti</span>
              <span><i style="background:#C8A96E"></i> Interessi maturati</span>
            </div>
            <p class="calc__note">Simulazione a scopo puramente illustrativo ed educativo, al lordo di costi e fiscalità: non costituisce consulenza personalizzata, offerta o promessa di rendimento. I rendimenti passati non sono indicativi di quelli futuri e il capitale investito è soggetto a rischio. Metodologia di calcolo coerente con il Calcolatore dell'interesse di Banca d'Italia (capitalizzazione mensile, versamenti a fine periodo).</p>
          </div>
        </div>
        <div class="calc__cta reveal">
          <a href="contatti.html" class="btn btn--primary">Costruiamo il tuo piano reale</a>
        </div>
      </div>
    </section>

{cta_band("Riconosci la tua situazione in uno di questi momenti?",
          "Il primo passo è una conversazione conoscitiva: capiamo insieme se e come posso esserti utile.")}
  </main>
''' + FOOTER

# ============================================================ PER LE IMPRESE
pages["per-le-imprese.html"] = head(
    "Per le imprese — Pianificazione finanziaria, TFM e TFR | Matteo Notario",
    "Pianificazione finanziaria d'impresa e previdenza aziendale (TFM per amministratori, TFR per dipendenti): due leve strategiche, un unico interlocutore.",
    "per-le-imprese.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Per le imprese</p>
        <h1 class="reveal d1">Tre leve strategiche,<br>un unico interlocutore.</h1>
        <p class="reveal d2">
          Aiuto imprenditori e PMI a trasformare liquidità, previdenza aziendale e formazione
          finanziaria in strumenti di crescita, tutela e continuità. Un unico interlocutore
          per collegare impresa, persone e patrimonio familiare.
        </p>
      </div>
    </section>

    <section class="pain section">
      <div class="container">
        <p class="section__eyebrow reveal">I nodi tipici</p>
        <h2 class="section__title reveal">Ti riconosci in almeno<br>uno di questi nodi?</h2>
        <div class="pain__grid">
          <article class="pain__card reveal">
            <span class="pain__num">01</span>
            <h3>La liquidità dorme sul conto</h3>
            <p>Cassa che resta ferma senza una strategia non è prudenza: è valore che non lavora, opportunità rimandate e decisioni lasciate in sospeso.</p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">02</span>
            <h3>TFM e TFR trattati come adempimenti</h3>
            <p>Accantonamenti e previdenza aziendale possono diventare leve fiscali, patrimoniali e di continuità, non solo voci da gestire.</p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">03</span>
            <h3>Impresa e patrimonio personale confusi</h3>
            <p>Quando azienda, famiglia e patrimonio si sovrappongono, ogni scelta pesa di più. Serve una regia che tenga insieme protezione, fiscalità e obiettivi.</p>
          </article>
          <article class="pain__card reveal">
            <span class="pain__num">04</span>
            <h3>Vendere o acquisire, ma da dove si parte?</h3>
            <p>Cessioni e acquisizioni aziendali: decisioni che capitano poche volte nella vita di un'impresa, ma affrontarle senza un orientamento e interlocutori qualificati significa negoziare al buio.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="calc section" id="la-cassa-che-dorme">
      <div class="container">
        <p class="section__eyebrow reveal">Prova con i numeri della tua azienda</p>
        <h2 class="section__title reveal">La cassa che dorme <span class="title-accent">ha un costo.</span></h2>
        <p class="section__intro reveal">
          Confronta due scenari sulla liquidità eccedente il fabbisogno operativo:
          lasciarla ferma a subire l'inflazione, oppure darle un compito con un'ipotesi prudente di impiego.
        </p>
        <div class="calc__panel reveal">
          <div class="calc__controls">
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="bizCapNum">Liquidità eccedente il fabbisogno</label>
                <span class="calc__value"><input type="number" id="bizCapNum" value="200000" min="0"><span class="calc__unit">€</span></span>
              </div>
              <input type="range" class="calc__range" id="bizCap" min="50000" max="5000000" step="10000" value="200000" aria-label="Liquidità eccedente il fabbisogno">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="bizYearsNum">Orizzonte</label>
                <span class="calc__value"><input type="number" id="bizYearsNum" value="7" min="0"><span class="calc__unit">anni</span></span>
              </div>
              <input type="range" class="calc__range" id="bizYears" min="1" max="15" step="1" value="7" aria-label="Orizzonte">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="bizInfNum">Inflazione media annua</label>
                <span class="calc__value"><input type="number" id="bizInfNum" value="2.5" min="0"><span class="calc__unit">%</span></span>
              </div>
              <input type="range" class="calc__range" id="bizInf" min="0" max="15" step="0.5" value="2.5" aria-label="Inflazione media annua">
            </div>
            <div class="calc__control">
              <div class="calc__control-head">
                <label for="bizRetNum">Ipotesi di impiego prudente</label>
                <span class="calc__value"><input type="number" id="bizRetNum" value="3" min="0"><span class="calc__unit">%</span></span>
              </div>
              <input type="range" class="calc__range" id="bizRet" min="0" max="5" step="0.5" value="3" aria-label="Ipotesi di impiego prudente">
            </div>
          </div>
          <div class="calc__results">
            <div>
              <div class="calc__bar-label"><span>Cifra nominale sul conto</span><strong id="bizNom">—</strong></div>
              <div class="calc__bar calc__bar--nominal"><span id="bizNomBar"></span></div>
            </div>
            <div>
              <div class="calc__bar-label"><span>Potere d'acquisto reale se resta ferma</span><strong id="bizStill">—</strong></div>
              <div class="calc__bar calc__bar--real"><span id="bizStillBar"></span></div>
            </div>
            <div>
              <div class="calc__bar-label"><span>Valore reale con impiego prudente</span><strong id="bizInvest">—</strong></div>
              <div class="calc__bar calc__bar--invest"><span id="bizInvestBar"></span></div>
            </div>
            <div class="calc__headline">
              <span class="calc__headline-label">Differenza tra i due scenari, in potere d'acquisto</span>
              <span class="calc__headline-value is-pos" id="bizDiff">+ 0 €</span>
            </div>
            <p class="calc__note">Simulazione a scopo puramente illustrativo ed educativo, al lordo di costi e fiscalità: non costituisce consulenza personalizzata, offerta o promessa di rendimento. Ogni impiego della liquidità aziendale va valutato rispetto a fabbisogni, vincoli di bilancio e profilo dell'impresa.</p>
          </div>
        </div>
        <div class="calc__cta reveal">
          <a href="contatti.html" class="btn btn--primary">Analizziamo la tua tesoreria</a>
        </div>
      </div>
    </section>

    <section class="statement" style="padding: 5.5rem 0;">
      <div class="container">
        <blockquote class="statement__quote reveal" style="max-width: 42ch; font-size: clamp(1.3rem, 2.5vw, 1.9rem);">
          Da questi nodi nasce il mio lavoro: trasformare liquidità, previdenza aziendale
          e decisioni straordinarie in <span class="statement__accent">una strategia leggibile</span>
          per l'impresa, l'imprenditore e il patrimonio familiare.
        </blockquote>
      </div>
    </section>

    <section class="section" style="padding-top: 0;">
      <div class="container">
        <div class="pillars">
          <article class="pillar reveal">
            <span class="pillar__tag">Leva 01</span>
            <h3>Pianificazione finanziaria d'impresa</h3>
            <p>Dare alla liquidità un ruolo nel piano dell'impresa, con orizzonti e protezioni coerenti con flussi e obiettivi — dalla gestione ordinaria alle operazioni straordinarie.</p>
            <ul>
              <li><strong>Gestione della liquidità aziendale</strong></li>
              <li><strong>Separazione e protezione</strong> tra impresa e patrimonio personale</li>
              <li><strong>Continuità e passaggio generazionale</strong></li>
              <li><strong>Operazioni straordinarie</strong> — primo orientamento su cessioni e acquisizioni, con accesso a partner specializzati, fino alla gestione del capitale che ne deriva.</li>
            </ul>
          </article>
          <article class="pillar reveal">
            <span class="pillar__tag">Leva 02</span>
            <h3>Previdenza aziendale: TFM e TFR</h3>
            <p>Trasformare un adempimento in una leva fiscale e finanziaria — per l'azienda e per le persone.</p>
            <ul>
              <li><strong>TFM per amministratori di PMI</strong></li>
              <li><strong>Gestione efficiente del TFR</strong> dei dipendenti</li>
              <li><strong>Welfare previdenziale</strong> che fidelizza</li>
            </ul>
          </article>
          <article class="pillar reveal">
            <span class="pillar__tag">Leva 03</span>
            <h3>Formazione in azienda</h3>
            <p>Educazione finanziaria e previdenziale su misura: momenti di formazione, non di vendita.</p>
            <ul>
              <li><strong>Sessioni per i dipendenti</strong> — risparmio, investimenti, TFR</li>
              <li><strong>Workshop per amministratori</strong> — TFM e remunerazione</li>
              <li><strong>In presenza o da remoto</strong>, singole sessioni o percorsi</li>
            </ul>
          </article>
        </div>

        <div class="business__stats">
          <div class="business__stat reveal">
            <span class="business__stat-num" data-count="3">0</span>
            <span class="business__stat-label">Aree di intervento integrate: finanza d'impresa, previdenza, formazione</span>
          </div>
          <div class="business__stat reveal">
            <span class="business__stat-num" data-count="4">0</span>
            <span class="business__stat-label">Fasi del metodo integrate: dalla diagnosi alla governance</span>
          </div>
          <div class="business__stat reveal">
            <span class="business__stat-num" data-count="1">0</span>
            <span class="business__stat-label">Interlocutore per impresa, imprenditore e famiglia</span>
          </div>
        </div>
      </div>
    </section>

{cta_band("Parliamone per la tua azienda.",
          "Un primo confronto per capire dove la finanza e la previdenza aziendale possono creare valore — per l'impresa e per le persone.")}
  </main>
''' + FOOTER

# ============================================================ ARTICOLI
pages["articoli.html"] = head(
    "Articoli — Matteo Notario, Consulenza Patrimoniale",
    "Riflessioni e approfondimenti su pianificazione patrimoniale, decisioni finanziarie e finanza d'impresa. Scritti da Matteo Notario.",
    "articoli.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Articoli</p>
        <h1 class="reveal d1">Idee per decidere meglio.</h1>
        <p class="reveal d2">
          Riflessioni su patrimonio, decisioni finanziarie e mercati:
          approfondimenti chiari e concreti, per chi vuole capire prima di decidere.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="articles__grid">
          <!-- TEMPLATE ARTICOLO: duplica questo blocco per ogni nuovo pezzo -->
          <a href="articolo-esempio.html" class="article-card reveal">
            <span class="article-card__meta">Pianificazione · 5 min</span>
            <h3>Titolo del tuo primo articolo</h3>
            <p>Una sintesi di due righe che anticipa il contenuto e invoglia alla lettura, senza svelare tutto.</p>
            <span>Leggi l'articolo →</span>
          </a>
          <a href="articolo-esempio.html" class="article-card reveal">
            <span class="article-card__meta">Mercati · 4 min</span>
            <h3>Titolo del tuo secondo articolo</h3>
            <p>Una sintesi di due righe che anticipa il contenuto e invoglia alla lettura, senza svelare tutto.</p>
            <span>Leggi l'articolo →</span>
          </a>
          <a href="articolo-esempio.html" class="article-card reveal">
            <span class="article-card__meta">Imprese · 6 min</span>
            <h3>Titolo del tuo terzo articolo</h3>
            <p>Una sintesi di due righe che anticipa il contenuto e invoglia alla lettura, senza svelare tutto.</p>
            <span>Leggi l'articolo →</span>
          </a>
        </div>
      </div>
    </section>

{cta_band("Preferisci parlarne di persona?",
          "Gli articoli danno spunti; una conversazione dà risposte sulla tua situazione specifica.")}
  </main>
''' + FOOTER

# ============================================================ ARTICOLO TEMPLATE
pages["articolo-esempio.html"] = head(
    "Titolo dell'articolo — Matteo Notario",
    "Descrizione dell'articolo in 150 caratteri circa, per Google e per le anteprime social.",
    "articolo-esempio.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Pianificazione · 5 min di lettura · [DATA]</p>
        <h1 class="reveal d1">Titolo dell'articolo:<br>chiaro, concreto, utile.</h1>
      </div>
    </section>

    <article class="container article-body">
      <p><strong>Questo è un template.</strong> Sostituisci questo testo con il tuo articolo. Il primo paragrafo deve rispondere subito alla domanda: perché il lettore dovrebbe continuare?</p>
      <h2>Un sottotitolo che struttura il ragionamento</h2>
      <p>Corpo del testo. Scrivi come parleresti a un cliente: frasi brevi, esempi concreti, niente gergo inutile. Un articolo utile costruisce più fiducia di dieci slogan.</p>
      <blockquote>Una frase chiave dell'articolo, messa in evidenza per chi legge in diagonale.</blockquote>
      <p>Chiudi ogni articolo con un'implicazione pratica: cosa dovrebbe fare — o smettere di fare — il lettore dopo averlo letto.</p>
    </article>

{cta_band("Questo tema riguarda la tua situazione?",
          "Parliamone: una prima conversazione conoscitiva, senza impegno.")}
  </main>
''' + FOOTER

# ============================================================ CONTATTI
pages["contatti.html"] = head(
    "Contatti — Matteo Notario, Consulente Finanziario",
    "Prenota una prima conversazione conoscitiva, gratuita e senza impegno. Rispondo entro 24 ore lavorative.",
    "contatti.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Contatti</p>
        <h1 class="reveal d1">Una conversazione,<br>nessun impegno.</h1>
      </div>
    </section>

    <section class="contact section">
      <div class="container contact__inner">
        <div class="contact__text">
          <p class="reveal">
            30 minuti per capire la tua situazione e dirti — con onestà — se e come posso
            esserti utile. Se non sono la persona giusta, te lo dico.
          </p>
          <ul class="contact__steps">
            <li class="reveal"><span>1</span> Compili il modulo (2 minuti)</li>
            <li class="reveal"><span>2</span> Ti ricontatto entro 24 ore lavorative</li>
            <li class="reveal"><span>3</span> Prima conversazione conoscitiva, gratuita</li>
          </ul>
          <div class="contact__direct">
            <a href="mailto:{EMAIL}" class="reveal">{MAIL_ICON}{EMAIL}</a>
            <a href="tel:{TEL_HREF}" class="reveal">{TEL_ICON}{TEL}</a>
            <a href="{LINKEDIN_URL}" target="_blank" rel="noopener" class="reveal">{LI_ICON}Profilo LinkedIn</a>
          </div>
        </div>
        <form class="contact__form reveal" id="contactForm" action="invia.php" method="POST" novalidate>
          <input type="text" name="sito_web" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;" aria-hidden="true">
          <div class="form__row">
            <div class="form__group">
              <label for="nome">Nome e cognome *</label>
              <input type="text" id="nome" name="nome" required autocomplete="name">
            </div>
            <div class="form__group">
              <label for="email">Email *</label>
              <input type="email" id="email" name="email" required autocomplete="email">
            </div>
          </div>
          <div class="form__row">
            <div class="form__group">
              <label for="telefono">Telefono</label>
              <input type="tel" id="telefono" name="telefono" autocomplete="tel">
            </div>
            <div class="form__group">
              <label for="situazione">La tua situazione *</label>
              <select id="situazione" name="situazione" required>
                <option value="" disabled selected>Seleziona…</option>
                <option>Voglio pianificare il mio patrimonio</option>
                <option>Cerco rendimenti con metodo</option>
                <option>Voglio una diagnosi gratuita del mio portafoglio</option>
                <option>Ho ricevuto un'eredità</option>
                <option>Ho venduto un'azienda</option>
                <option>Ho concluso un'operazione immobiliare</option>
                <option>Sono un'azienda (finanza, previdenza, formazione)</option>
                <option>Altro</option>
              </select>
            </div>
          </div>
          <div class="form__group">
            <label for="messaggio">Cosa vorresti approfondire?</label>
            <textarea id="messaggio" name="messaggio" rows="4"></textarea>
          </div>
          <label class="form__privacy">
            <input type="checkbox" name="privacy" required>
            <span>Ho letto l'<a href="privacy.html">informativa privacy</a> e acconsento al trattamento dei dati per essere ricontattato. *</span>
          </label>
          <button type="submit" class="btn btn--primary btn--full">Invia la richiesta</button>
          <p class="form__status" id="formStatus" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

    <section class="faq section">
      <div class="container">
        <p class="section__eyebrow reveal">Domande frequenti</p>
        <h2 class="section__title reveal">Alcune domande che ricevo spesso.</h2>
        <div class="faq__list reveal">
          <details class="faq__item" open>
            <summary>L'incontro conoscitivo ha un costo?<span class="faq__icon">+</span></summary>
            <p>No, è gratuito e senza impegno. Possiamo incontrarci di persona oppure in videochiamata. Serve a capire la tua situazione, i tuoi obiettivi e se posso esserti concretamente utile.</p>
          </details>
          <details class="faq__item">
            <summary>La diagnosi di portafoglio ha un costo?<span class="faq__icon">+</span></summary>
            <p>No, è gratuita. Analizzo come è composto e gestito oggi il tuo patrimonio, mettendo in evidenza costi, rischi, diversificazione e coerenza con i tuoi obiettivi.</p>
          </details>
          <details class="faq__item">
            <summary>Devo trasferire i miei investimenti per ricevere la diagnosi?<span class="faq__icon">+</span></summary>
            <p>No. La diagnosi viene effettuata sul portafoglio esistente, senza dover trasferire nulla. Al termine riceverai un'analisi scritta e sarai tu a decidere liberamente come utilizzarla.</p>
          </details>
          <details class="faq__item">
            <summary>Lavori per una banca?<span class="faq__icon">+</span></summary>
            <p>Opero come consulente finanziario abilitato all'offerta fuori sede, iscritto all'Albo unico OCF, per FinecoBank. Prima di iniziare chiarisco sempre il mio ruolo, il metodo di lavoro e le condizioni applicabili.</p>
          </details>
          <details class="faq__item">
            <summary>Come vengono remunerati i servizi?<span class="faq__icon">+</span></summary>
            <p>L'incontro conoscitivo e la diagnosi iniziale sono gratuiti. Per gli eventuali servizi successivi, modalità di remunerazione e costi vengono illustrati e definiti con trasparenza prima di iniziare.</p>
          </details>
          <details class="faq__item">
            <summary>Ho un patrimonio contenuto: ha comunque senso rivolgersi a un consulente?<span class="faq__icon">+</span></summary>
            <p>Dipende dai tuoi obiettivi e dalla complessità delle decisioni da prendere, non soltanto dall'importo disponibile. Nel primo incontro valutiamo concretamente se una consulenza può offrirti un beneficio reale. Se non posso aggiungere valore, te lo dico con chiarezza.</p>
          </details>
          <details class="faq__item">
            <summary>Dove lavori?<span class="faq__icon">+</span></summary>
            <p>Il mio ufficio è a Torino, ma seguo clienti in tutta Italia anche tramite incontri in videochiamata.</p>
          </details>
          <details class="faq__item">
            <summary>Quando è il momento giusto per iniziare a investire?<span class="faq__icon">+</span></summary>
            <p>Prima di investire bisogna chiarire obiettivi, orizzonte temporale, disponibilità economiche e rischi sostenibili. Il momento giusto nasce da una strategia personale, non dal tentativo di prevedere il prossimo movimento dei mercati.</p>
          </details>
          <details class="faq__item">
            <summary>Su cosa conviene investire oggi?<span class="faq__icon">+</span></summary>
            <p>Non esiste uno strumento adatto a tutti. Il punto di partenza non è scegliere un prodotto, ma capire quale obiettivo deve finanziare il patrimonio. Solo dopo si possono individuare strumenti coerenti con la strategia, il tempo disponibile e il rischio sostenibile.</p>
          </details>
        </div>
      </div>
    </section>
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "L'incontro conoscitivo ha un costo?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No, è gratuito e senza impegno. Possiamo incontrarci di persona oppure in videochiamata. Serve a capire la tua situazione, i tuoi obiettivi e se posso esserti concretamente utile."
      }}
    }},
    {{
      "@type": "Question",
      "name": "La diagnosi di portafoglio ha un costo?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No, è gratuita. Analizzo come è composto e gestito oggi il tuo patrimonio, mettendo in evidenza costi, rischi, diversificazione e coerenza con i tuoi obiettivi."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Devo trasferire i miei investimenti per ricevere la diagnosi?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No. La diagnosi viene effettuata sul portafoglio esistente, senza dover trasferire nulla. Al termine riceverai un'analisi scritta e sarai tu a decidere liberamente come utilizzarla."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Lavori per una banca?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Opero come consulente finanziario abilitato all'offerta fuori sede, iscritto all'Albo unico OCF, per FinecoBank. Prima di iniziare chiarisco sempre il mio ruolo, il metodo di lavoro e le condizioni applicabili."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Come vengono remunerati i servizi?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "L'incontro conoscitivo e la diagnosi iniziale sono gratuiti. Per gli eventuali servizi successivi, modalità di remunerazione e costi vengono illustrati e definiti con trasparenza prima di iniziare."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Ho un patrimonio contenuto: ha comunque senso rivolgersi a un consulente?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Dipende dai tuoi obiettivi e dalla complessità delle decisioni da prendere, non soltanto dall'importo disponibile. Nel primo incontro valutiamo concretamente se una consulenza può offrirti un beneficio reale. Se non posso aggiungere valore, te lo dico con chiarezza."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Dove lavori?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Il mio ufficio è a Torino, ma seguo clienti in tutta Italia anche tramite incontri in videochiamata."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Quando è il momento giusto per iniziare a investire?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Prima di investire bisogna chiarire obiettivi, orizzonte temporale, disponibilità economiche e rischi sostenibili. Il momento giusto nasce da una strategia personale, non dal tentativo di prevedere il prossimo movimento dei mercati."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Su cosa conviene investire oggi?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Non esiste uno strumento adatto a tutti. Il punto di partenza non è scegliere un prodotto, ma capire quale obiettivo deve finanziare il patrimonio. Solo dopo si possono individuare strumenti coerenti con la strategia, il tempo disponibile e il rischio sostenibile."
      }}
    }}
  ]
}}
    </script>
  </main>
''' + FOOTER

# ============================================================ PRIVACY
pages["privacy.html"] = head(
    "Privacy Policy — Matteo Notario",
    "Informativa sul trattamento dei dati personali.",
    "privacy.html"
) + NAV + f'''
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="page-hero__eyebrow reveal">Note legali</p>
        <h1 class="reveal d1">Privacy &amp; Cookie Policy</h1>
      </div>
    </section>
    <section class="container article-body">
      <p><strong>DA VALIDARE PRIMA DEL GO-LIVE</strong> con un consulente privacy/DPO: struttura di base, non un testo definitivo.</p>
      <h2>Titolare del trattamento</h2>
      <p>Matteo Notario — [indirizzo], P.IVA [XXXXXXXXXXX] — email: {EMAIL}</p>
      <h2>Dati raccolti e finalità</h2>
      <p>Tramite il modulo di contatto: nome, email, telefono (facoltativo), descrizione della situazione. Base giuridica: consenso (art. 6.1.a GDPR). Finalità: ricontattare l'interessato. Nessun uso di marketing senza consenso specifico.</p>
      <h2>Conservazione e diritti</h2>
      <p>I dati sono conservati per il tempo necessario a gestire la richiesta. Diritti ex artt. 15-22 GDPR esercitabili scrivendo a {EMAIL}.</p>
      <h2 id="cookie">Cookie</h2>
      <p>Questo sito non utilizza cookie di profilazione. [Aggiornare se verranno installati strumenti di analytics: in tal caso è necessario un banner cookie conforme.]</p>
    </section>
  </main>
''' + FOOTER

# ---------------------------------------------------------- scrittura file
import os
os.chdir("/home/claude/sito2")
for name, html in pages.items():
    with open(name, "w") as f:
        f.write(html)
    print("scritta:", name)
