while True:
    try:
        altura = float(input("Digite sua altura em metros: "))
        if altura > 0:
            break
        else:
            print("A altura deve ser maior que zero.")
    except:
        print("Digite apenas números.")

print("Altura válida:", altura)