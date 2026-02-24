while True:
    try:
        valor = int(input("Qual o valor desejado do saque? "))

        quantdin = valor

        if quantdin > 1000:
            print("Valor inválido")
            continue
        else:
            break
        
    except ValueError:
        print("O valor sacado deve ser abaixo de 1000 reais.")

print("Valor resgatado:", valor)