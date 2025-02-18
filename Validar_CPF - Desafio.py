# cpf = 168.995.350-09


contagem = 10
resultado = 0
nove_digitos = [1, 6, 8, 9, 9, 5, 3, 5, 0]
n = int
for n in nove_digitos:
    resultado += n * contagem
    contagem-=1
    print(resultado)


    if contagem == 1:
        resultado = 11 - (resultado % 11)
        if resultado >= 9:
            resultado = 0
            contagem = 11
            nove_digitos.append(resultado)
            continue





















































