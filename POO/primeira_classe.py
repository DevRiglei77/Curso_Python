class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def Comprimentar(self):
        print(f"Olá {self.nome}")


p1 = Pessoa("Riglei",24)

print(p1.Comprimentar())