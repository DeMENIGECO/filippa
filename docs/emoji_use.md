# Emoji Use

Questa opzione permette di controllare l'utilizzo delle emoji nelle risposte di Filippa.

---

## Configurazione

La configurazione si trova nel file principale:

```python
emoji_use = 1
```

Il valore può essere modificato in base alla modalità desiderata.

---

## Valori disponibili

### `1` - Moderato

Attiva le risposte con emoji.

Esempio:

```text
Tu: ciao
Filippa: Ciao 👋! Sono Filippa, e sono qui per aiutarti!
```

Questa modalità rende la conversazione più amichevole e naturale.

---

### `0` - Nessuno

Disattiva le emoji nelle risposte.

Esempio:

```text
Tu: ciao
Filippa: Ciao! Sono Filippa, e sono qui per aiutarti!
```

Questa modalità è consigliata per output più puliti.

---

## Valori non validi

Se viene inserito un valore diverso da `0` o `1`, Filippa genera un errore:

```text
[Filippa] Valore uso emoji invalido: VALORE
Leggi: docs/ai/emoji_use.md
```

---

## Note tecniche

Filippa utilizza due dizionari di risposte:

- `meta.me_responses` → risposte con emoji
- `meta.ne_responses` → risposte senza emoji

La selezione avviene automaticamente durante l'avvio.
