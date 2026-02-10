while True:
    nome = input("Digite seu nome: ").strip()

    if nome =="":
        print("O nome não pode ser vazio")
    else:
        break

print("Nome", nome)