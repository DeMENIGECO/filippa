# FipCode

Un generatore di file basato su **Filippa**.

FipCode è un componente del progetto Filippa che permette di generare file
utilizzando il sistema di gestione e le funzionalità messe a disposizione
dall'agente.

> [!WARNING]
> FipCode è attualmente in fase di test. Il comportamento e le funzionalità
> possono cambiare nelle versioni future.

---

## Utilizzo

Per avviare FipCode, esegui:

```bash
python -m fipcode.fipcode
```

FipCode verrà avviato direttamente tramite il modulo Python.

---

## Requisiti

Per utilizzare FipCode è necessario avere:

- Python installato;
- Filippa configurata correttamente;
- il pacchetto `fipcode` disponibile nel progetto.

---

## Struttura

FipCode fa parte dell'ecosistema di Filippa e viene organizzato come modulo
Python:

```text
fipcode/
    ├── fipcode.py
    ├── fs_pull_layer.py
    └── fs_meta_resp.xml
```

---

## Stato del progetto

FipCode è attualmente in fase di sviluppo e test.

Funzionalità, API e struttura interna potrebbero cambiare senza preavviso
prima di una versione stabile.

---

## Documentazione

La documentazione relativa a FipCode e agli altri componenti di Filippa è
disponibile nella directory `docs/`.

---

## Filippa

FipCode è sviluppato come parte del progetto **Filippa**, un agente AI
scritto in Python.
