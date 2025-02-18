
def cria_funcao(funcao):
    def valida_numeros(x,y):
        if x < 0 or y < 0:
            raise ValueError ("O y e nem o x podem ser menor que zero")
        return funcao(x,y)
    return valida_numeros

@cria_funcao

def soma(x,y):
    return x+y


