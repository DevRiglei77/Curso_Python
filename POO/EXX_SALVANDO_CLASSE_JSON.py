import json

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def Comprimentar(self):
        print(f"Olá {self.nome}")

p1 = Pessoa(nome="Riglei",idade=24)


with open("minha_classe.json",mode='w',encoding='utf-8') as arquivo:
    json.dump(p1.__dict__,arquivo,ensure_ascii=True)


with open("minha_classe.json",mode='r',encoding='utf-8') as arquivo:
    p1 = json.load(arquivo)
    p1 = Pessoa(**p1)

