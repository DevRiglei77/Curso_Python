class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def Comprimentar(self):
        print(f"Olá {self.nome}")

    @classmethod
    def cria_pessoa_anonima(cls,idade):
        return cls('Anônima',idade)

#o exemplo o metodo de classe serviu para eu criar uma pessoa anonima, onde o metodo recebe
# a propria classe (cls) e instancia sem o self os atributos nome e idade

p1 = Pessoa.cria_pessoa_anonima(idade=24)
print(p1.nome)
print(p1.idade)