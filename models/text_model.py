class TextModel:
    def __init__(self):
        self._text = ""

    def set_text(self, text):
        # Lógica de negócios e validação ficariam aqui
        self._text = text

    def get_text(self):
        return self._text