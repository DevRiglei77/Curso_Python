# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

produtos_com_aumento = copy.deepcopy(produtos)

for produto in produtos_com_aumento:
    produto['preco'] = produto['preco'] * 10 / 100 + produto['preco']
    produtos_ordenados_por_preco = copy.deepcopy(produtos_com_aumento)
    produtos_ordenados_por_nome = copy.deepcopy(produtos_com_aumento)
    produtos_ordenados_por_preco.sort(key=lambda produto: produto['preco'])
    produtos_ordenados_por_nome.sort(key=lambda produto: produto['nome'],reverse=True)

print(produtos_ordenados_por_nome)
print(produtos_ordenados_por_preco)



