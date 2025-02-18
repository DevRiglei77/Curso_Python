from typing import List, Any

num = 0
posiçao = 0
lista = []
for num in range(0,5):
    num = int(input("Digite o valor para a posição {} ".format(posiçao)))
    lista.insert(posiçao , num)
    posiçao+=1

print("O menor valor digitado foi {} na posição {} e o maior foi {} na posição {} ".format(min(lista),lista.index(min(lista)),max(lista),lista.index(max(lista))))
# print("Nas posições {} e {} ".format(lista.index(min(lista)),lista.index(max(lista))),end='')

