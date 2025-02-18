# Função len, que conta o numero de caracteres...


nome = input('Digite seu nome ')
sobrenome = input("Digite seu sobrenome ")

qntd_caracteres = len(nome) + len(sobrenome)

print("Seu nome contém {} letras ".format(qntd_caracteres))

print(nome.__len__() + sobrenome.__len__())