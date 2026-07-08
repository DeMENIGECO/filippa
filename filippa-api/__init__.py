class Bot:  
    def __init__(self):
        """Inizzializza il bot"""
        self.name = "filippa"
        self.emojiuse = 1
        self.mode = 0
        return None
        
    def responses_dict(self):
        """Ritorna il dizionario in base all'emoji use adatto"""
        me_responses = {
            "ciao": "Ciao 👋! Sono " + self.name.capitalize() + ", e sono qui per aiutarti!",
            "come stai": "Io sto bene 😄, e tu?",
            "io sto bene": "Anch'io 😄!",
            "sono triste": "Oh 😢! Come posso renderti felice?"
        }
        ne_responses = {
            "ciao": "Ciao! Sono " + self.name.capitalize() + ", e sono qui per aiutarti!",
            "come stai": "Io sto bene, e tu?",
            "io sto bene": "Anch'io!",
            "sono triste": "Oh! Come posso renderti felice?"
        }
        if self.emojiuse == 1:
            return me_responses
        elif self.emojiuse == 0:
            return ne_emoji
        else:
            raise ValueError("[FilippaAPI] Uso invalido di emoji: leggi docs/ai/emoji_use.md")
            return None
            
    def ask(self, asked):
        """Chiede una domanda al bot"""
        asked = asked.strip().upper()
        if key in responses_dict():
            print(responses_dict[asked])
        else:
            print("Non so rispondere!")
        
        
    
