while True:
    try:
        parcelas = int(input("Digite o número de parcelas: "))
        if parcelas >= 1 and parcelas <= 12:
            break
        else:
            print("Digite um número entre 1 e 12.")
    except:
        print("Digite apenas números.")

print("Parcelas escolhidas:", parcelas)