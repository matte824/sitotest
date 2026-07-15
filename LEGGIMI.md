# Sito Matteo Notario — Guida rapida (v3)

## Struttura
```
index.html / chi-sono.html / metodo.html / quando-intervengo.html /
per-le-imprese.html / articoli.html / articolo-esempio.html (template) /
contatti.html / privacy.html
css/fonts.css    → font SELF-HOSTED (GDPR: nessuna chiamata a server Google)
css/style.css    → colori e font in :root
js/main.js       → animazioni, nav, form
fonts/           → file .woff2 dei font
img/             → logo, foto, og-cover
invia.php        → gestione form SENZA servizi terzi (richiede hosting PHP)
build.py         → rigenera le pagine (header/footer in un punto solo)
```

## Form di contatto (invia.php)
- I dati vanno dal sito al TUO server, che li inoltra a matteo.notario@pfafineco.it. Nessun soggetto terzo, nessun cookie.
- Da fare al go-live: in invia.php aggiorna FROM_EMAIL con una casella del tuo dominio (es. noreply@tuodominio.it) — molti hosting la richiedono per il recapito.
- Include honeypot anti-spam invisibile.

## Hosting — decisione presa insieme
Requisiti: zero gestione tecnica, articoli pubblicabili facilmente, GDPR semplice, Italia.
→ **Hosting WordPress Gestito Aruba** (data center in Italia) + conversione di questo sito in tema WordPress custom (prossimo step con Claude). In WP il form userà un plugin che invia dal server (equivalente a invia.php).
In attesa della conversione, questo sito statico funziona su qualsiasi hosting PHP (es. Aruba Hosting Linux).

## Checklist go-live
1. Sostituire `tuodominio.it` (meta tag + invia.php)
2. Approvazione compliance Fineco del sito (in particolare: parcella, confronti)
3. Validare privacy.html con consulente privacy
4. Test invio form dopo la pubblicazione

## Nuovo articolo (versione statica)
Duplica articolo-esempio.html → rinomina → aggiorna testi → aggiungi card in articoli.html.
(Con WordPress: si scriverà dall'editor, senza toccare codice.)
