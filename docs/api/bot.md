# Bot

La classe principale di Filippa.

## Creazione

```python
from filippa_api import Bot

bot = Bot()
```

## Attributi

### `name`

Nome del bot.

**Tipo:** `str`

```python
bot.name = "Filippa"
```

---

### `emojiuse`

Abilita o disabilita l'uso delle emoji.

**Tipo:** `int`

| Valore | Significato |
|--------:|-------------|
| `0` | Moderato |
| `1` | Abilitato |

```python
bot.emojiuse = 1
```

---

## Metodi

### `ask(text: str) -> str`

Invia un messaggio al bot e restituisce la risposta.

**Parametri**

- `text` (`str`): messaggio da inviare.

**Stampa**

- `str`: risposta del bot.

**Esempio**

```python
from filippa_api import Bot

bot = Bot()
bot.name = "Filippa"
bot.emojiuse = 1

bot.ask("Ciao")
```
