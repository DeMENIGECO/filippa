# Names

Questa opzione permette di configurare i nomi utilizzati da Filippa durante la conversazione.

I nomi vengono utilizzati per identificare l'utente, l'intelligenza artificiale e la modalità DeepAgent.

---

## Configurazione

La configurazione si trova nel file principale:

```python
user = "tu"
ai = meta.name.capitalize()
deep = "[DeepAgent] " + ai
```

---

## Nomi disponibili

### User

La variabile `user` rappresenta il nome mostrato per l'utente.

Esempio:

```python
user = "tu"
```

Output:

```text
Tu: ciao
```

È possibile modificarla con un nome personalizzato.

Esempio:

```python
user = "DomeniGeco"
```

Output:

```text
DomeniGeco: ciao
```

---

### AI

La variabile `ai` rappresenta il nome principale dell'assistente.

Il nome viene preso automaticamente da `meta.name` e viene convertito con la prima lettera maiuscola.

Esempio:

```python
name = "filippa"
```

Risultato:

```text
Filippa
```

Output:

```text
Filippa: Ciao! Sono Filippa, e sono qui per aiutarti!
```

---

### DeepAgent

La variabile `deep` rappresenta il nome utilizzato quando la modalità DeepAgent è attiva.

Viene creato automaticamente aggiungendo il prefisso `[DeepAgent]`.

Esempio:

```text
[DeepAgent] Filippa
```

Output:

```text
[DeepAgent] Filippa: Ciao! Sono Filippa, e sono qui per aiutarti!
```

---

## Note tecniche

La gestione dei nomi permette di modificare l'identità visualizzata di Filippa senza modificare il funzionamento interno dell'agente.

Per cambiare il nome dell'assistente è sufficiente modificare:

```python
name = "filippa"
```

nel file `meta.py`.
