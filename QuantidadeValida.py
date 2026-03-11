while True:
    try:
        quantidade = int(input("Digite a quantidade de produtos: "))
        if quantidade > 0:
            break
        else:
            print("Digite um número inteiro positivo.")
    except:
        print("Digite apenas números.")

print("Quantidade informada:", quantidade)