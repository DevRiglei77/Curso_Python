class Programador:
    def __init__(self,nome,idade):
        self.nome =  nome
        self.idade = idade
        self._skil = None

    @property
    def skil(self):
        return self._skil

    @skil.setter
    def skil(self,skil):
        self._skil = skil

class Linguagens:
    def __init__(self,nome):
        self._nome = nome




riglei = Programador("Riglei",24)
python = Linguagens('Python')
riglei.skil = python
