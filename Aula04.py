num1 = input("Digite um numero ")
num2 = input("Digite outro numero ")

print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)

else:
    print("Erro")

