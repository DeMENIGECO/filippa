import meta

"""
Filippa v0.1.2
"""

#Uso delle emoji
#Leggi: docs/ai/emoji_use.md
emoji_use = 1

#Debug
#Leggi: docs/ai/debug.md
#Disattivalo in produzione!
debug = True

# Gestione risposte
#NON TOCCARE!
if emoji_use == 1:
    responses_dict = meta.me_responses
    str_use = "Moderato"
elif emoji_use == 0:
    responses_dict = meta.ne_responses
    str_use = "Nessuno"
else:
    raise ValueError(f"[Filippa] Valore uso emoji invalido: {emoji_use}\nLeggi: docs/ai/emoji_use.md")

#Nomi
#Leggi: docs/ux/names.md
user = "tu"
ai = meta.name.capitalize()
deep = "[DeepAgent] " + ai

#Avvio
#Leggi: docs/ai/start.md
#NON TOCCARE!
deepagent = False
if debug:
    print(
        "== AGENT INFO ==",
        f"\nUso emoji: {str_use} | ",
        "DeepAgent: Attivato" if deepagent else "DeepAgent: Disattivato",
        "\n==============="
    )
else:
    pass

while True:
    user_input = input(f"{user.capitalize()}: ")

    if user_input == "startDeepAgent":
        deepagent = True
        print(
            '[Filippa] DeepAgent Avviato. Iniziata nuova sessione con ".::deep:true"' if debug else "DeepAgent Avviato")
    else:
        outname = f"{deep}: " if deepagent else f"{ai}: "
        key = user_input.strip().lower()

        if key in responses_dict:
            print(outname + responses_dict[key])
        else:
            print(outname + "Non so rispondere!")
