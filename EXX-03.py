Nome = input("Digite seu nome ")

if len(Nome) <= 4:
    print("Seu nome é curto ")

elif len(Nome) >= 5 and len(Nome) <= 6:
    print("Seu nome é normal ")

elif len(Nome) > 6:
    print("Seu nome é muito grande ")
