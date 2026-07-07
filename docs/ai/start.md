# Start

Questa sezione descrive il sistema di avvio di Filippa e il comportamento iniziale dell'agente.

---

## Avvio

Quando Filippa viene avviata, vengono caricati:

- il nome dell'assistente;
- le impostazioni delle emoji;
- la modalità debug;
- il dizionario delle risposte;
- la configurazione dei nomi.

Dopo il caricamento della configurazione, Filippa è pronta a ricevere messaggi dall'utente.

---

## Configurazione iniziale

All'avvio viene inizializzata la modalità DeepAgent:

```python
deepagent = False
```

Questo significa che Filippa parte nella modalità normale.

Esempio:

```text
Tu: ciao
Filippa: Ciao 👋! Sono Filippa, e sono qui per aiutarti!
```

---

## DeepAgent

DeepAgent è una modalità speciale che può essere attivata durante una sessione.

Per avviarla, utilizzare il comando:

```text
startDeepAgent
```

Dopo l'attivazione, Filippa cambia il nome visualizzato:

```text
[DeepAgent] Filippa: Ciao 👋! Sono Filippa, e sono qui per aiutarti!
```

---

## Messaggio di avvio

Se la modalità debug è attiva, Filippa mostra informazioni aggiuntive:

```text
== AGENT INFO ==
Uso emoji: Moderato | DeepAgent: Disattivato
===============
```

Se il debug è disattivato, queste informazioni non vengono mostrate.

---

## Note tecniche

Il sistema di avvio è gestito direttamente da `filippa.py`.

Durante l'avvio non vengono modificate le risposte dell'agente: vengono solamente caricate le configurazioni necessarie al funzionamento.
