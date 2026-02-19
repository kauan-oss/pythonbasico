while True:
    try:
        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ")

        quantcarac = len(senha)

        if nome =="":
            print("O nome não pode estar vazio!")

        elif quantcarac < 6:
            print("Senha inválida. Escolha uma senha que tenha no mínimo 6 caracteres. Digite seu login novamente.")
        
        else:
            break

    except ValueError:
        print("A senha deve conter apenas 6 números")

print("Usuário Cadastrado:", nome)