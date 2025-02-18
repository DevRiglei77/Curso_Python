num1 = input("Digite um número inteiro ")

if num1.isnumeric():
    if int(num1) % 2 == 0:
        print("O {} é par ".format(num1))
    else:
        print("O {} é impar ".format(num1))

else:
    print("O {} não é inteiro ".format(num1))
