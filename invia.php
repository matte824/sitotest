<?php
/**
 * invia.php — Gestione del form di contatto SENZA servizi terzi.
 * I dati vengono inviati via email dal server di hosting a DEST_EMAIL
 * e non transitano da alcun soggetto esterno (GDPR-friendly).
 *
 * Requisito: hosting con PHP (Aruba, SiteGround, ecc.).
 * Se le email non arrivano: alcuni hosting richiedono che il mittente ($from)
 * sia una casella del proprio dominio — crea es. noreply@tuodominio.it e aggiorna sotto.
 */

declare(strict_types=1);

const DEST_EMAIL = 'matteo.notario@pfafineco.it';
const FROM_EMAIL = 'noreply@tuodominio.it'; // <-- aggiorna col tuo dominio reale

header('Content-Type: application/json; charset=utf-8');

// Solo richieste POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Metodo non consentito']);
    exit;
}

// Honeypot anti-spam: campo invisibile che i bot compilano e gli umani no
if (!empty($_POST['sito_web'] ?? '')) {
    // Fingiamo successo per non dare indizi ai bot
    echo json_encode(['ok' => true]);
    exit;
}

// Lettura e pulizia input
$pulisci = fn(string $v): string => trim(str_replace(["\r", "\n"], ' ', strip_tags($v)));

$nome      = $pulisci($_POST['nome'] ?? '');
$email     = $pulisci($_POST['email'] ?? '');
$telefono  = $pulisci($_POST['telefono'] ?? '');
$motivo    = $pulisci($_POST['motivo'] ?? '');
$altro     = $pulisci($_POST['altro'] ?? '');
$messaggio = trim(strip_tags($_POST['messaggio'] ?? ''));
$privacy   = isset($_POST['privacy']);

// Se il motivo è "Altro", l'argomento specificato diventa obbligatorio
if ($motivo === 'Altro') {
    $motivo = $altro !== '' ? 'Altro: ' . $altro : '';
}

// Validazione: tutti i campi sono obbligatori
if ($nome === '' || $telefono === '' || $motivo === '' || $messaggio === '' || !$privacy || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'error' => 'Dati mancanti o non validi']);
    exit;
}

// Composizione email
$oggetto = "Nuova richiesta dal sito — {$nome}";
$corpo = "Nuova richiesta di contatto dal sito web\n"
       . str_repeat('-', 44) . "\n"
       . "Nome:       {$nome}\n"
       . "Email:      {$email}\n"
       . "Telefono:   {$telefono}\n"
       . "Motivo:     {$motivo}\n"
       . str_repeat('-', 44) . "\n"
       . "Messaggio:\n" . ($messaggio ?: '—') . "\n"
       . str_repeat('-', 44) . "\n"
       . "Consenso privacy: sì | Data: " . date('d/m/Y H:i') . "\n";

$headers = [
    'From: Sito Web <' . FROM_EMAIL . '>',
    'Reply-To: ' . $nome . ' <' . $email . '>',
    'X-Mailer: PHP/' . phpversion(),
    'Content-Type: text/plain; charset=utf-8',
];

$inviata = mail(DEST_EMAIL, $oggetto, $corpo, implode("\r\n", $headers));

if ($inviata) {
    echo json_encode(['ok' => true]);
} else {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Invio non riuscito']);
}
