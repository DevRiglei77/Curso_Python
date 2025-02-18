# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades_siglas = []

# for indice,cidade in enumerate(cidades):
#     for sigla in siglas[indice:]:
#         cidades_siglas.append((cidade,sigla))
#         break

#outra solucao

# cidades_siglas = [
#
#     (cidades[i],siglas[i]) for i in range(min(len(cidades),len(siglas)))
# ]

#outra solucao

# zip pega dados da menor lista - que no caso é cidades
cidades_siglas = list(zip(cidades,siglas))

from itertools import zip_longest

cidades_siglas = list(zip_longest(cidades,siglas,fillvalue="Rio De Janeiro"))

print(cidades_siglas)