while True:
    try:
        idade = int(input("digite sua idade: "))
        if idade <= 0: 
            print("A idade deve ser maior que zero!!")
        else:
            break
    except ValueError:
        print("Digite uma idade válida!")

print("Sua idade é: ", idade)