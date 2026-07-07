import meta

"""
Filippa v0.1.0
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
print(
    "== AGENT INFO ==",
    f"\nUso emoji: {str_use} | ",
    "DeepAgent: Attivato" if deepagent else "DeepAgent: Disattivato",
    "\n==============="
)

while True:
    user_input = input(user.capitalize() + ": ")

    if user_input == "startDeepAgent":
        deepagent = True
        print('[Filippa] DeepAgent Avviato. Iniziata nuova sessione con ".::deep:true"' if debug else "DeepAgent Avviato")
    else:
        outname = f"{deep}: " if deepagent else f"{ai}: "
        if user_input.strip().lower() in responses_dict.keys:
            print(outname + responses_dict.rispostachiavevalorebasato)
        else:
            print(outname + "Non so rispondere!")
    
