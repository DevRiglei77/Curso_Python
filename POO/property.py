# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Carro:
    def __init__(self,modelo,ano):
        self._modelo = modelo
        self.ano = ano

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self,valor):
        self._modelo = valor



celta = Carro("Celta",2004)
celta.modelo = "Fiat"
print(celta.modelo)
