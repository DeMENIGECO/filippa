# Debug

Questa opzione permette di attivare o disattivare le informazioni di debug di Filippa.

La modalità debug è utile durante lo sviluppo per controllare lo stato dell'agente e verificare la configurazione attuale.

---

## Configurazione

La configurazione si trova nel file principale:

    debug = True

Il valore può essere modificato in base all'ambiente di utilizzo.

---

## Valori disponibili

### `True` - Attivato

Attiva le informazioni di debug.

All'avvio Filippa mostra informazioni aggiuntive:

    == AGENT INFO ==
    Uso emoji: Moderato | DeepAgent: Disattivato
    ===============

Inoltre, durante l'avvio del DeepAgent, mostra un messaggio dettagliato:

    [Filippa] DeepAgent Avviato. Iniziata nuova sessione con ".::deep:true"

Questa modalità è consigliata durante lo sviluppo.

---

### `False` - Disattivato

Disattiva le informazioni di debug.

Filippa mostra solo i messaggi necessari all'utente:

    DeepAgent Avviato

Questa modalità è consigliata per l'utilizzo in produzione.

---

## Nota importante

La modalità debug deve essere disattivata prima di distribuire Filippa agli utenti finali:

    debug = False

Lasciare il debug attivo può mostrare informazioni interne del sistema.

---

## Note tecniche

Il valore di `debug` controlla solamente la visualizzazione dei messaggi di sistema.

Non modifica:

- il sistema di risposte;
- il funzionamento del DeepAgent;
- la gestione delle emoji.
