lista = []
while True:
    num = int(input("Digite um número "))

    if num in lista:
        print('Valor já adicionado,não vou adicionar ')

    else:
       lista.append(num)
    R = input('Deseja continuar? [S/N] ')
    if  R == 'N':
        break
lista.sort()


print(lista)

