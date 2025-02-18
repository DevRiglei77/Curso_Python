horas = input("Que horas são? (0-23) ")

if int(horas) >= 0 and int(horas) <= 11:
    print("Bom dia! ")

elif int(horas) >= 12 and int(horas) <= 17:
    print("Boa tarde! ")

elif int(horas) >= 18 and int(horas) <= 23:
    print("Boa noite! ")

elif int(horas) < 0 or int(horas) > 23:
    print("Digite um horário valido ")
