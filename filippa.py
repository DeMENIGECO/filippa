import meta

"""
Filippa v0.1.0
"""

#Uso delle emoji
#Leggi: docs/ai/emoji_use.md
emoji_use = 1

# Gestione risposte
#NON TOCCARE!
if emoji_use == 1:
    responses_dict = meta.me_responses
elif emoji_use == 0:
    responses_dict = meta.ne_responses
else:
    raise ValueError(f"[Filippa] Valore uso emoji invalido: {emoji_use}\nLeggi: docs/ai/emoji_use.md")

#Nomi
#Leggi: docs/ux/names.md

