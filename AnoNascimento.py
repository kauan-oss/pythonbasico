while True:
    try:
        ano = int(input("Digite seu ano de nascimento: "))
        if ano > 1900 and ano <= 2026:
            break
        else:
            print("Digite um ano entre 1901 e 2026.")
    except:
        print("Digite apenas números.")

print("Ano de nascimento:", ano)