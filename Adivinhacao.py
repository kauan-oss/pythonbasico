print('*************************')
print('***Jogo da adivinhação***')
print('*************************')

numero_secreto = 67
total_tentativas = 3
rodada = 1

while ( rodada <= total_tentativas ):
    chute_str = input( "Digite o seu número: " )

    print( "Seu número é", chute_str )

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if( acertou ):
        print("Você acertou")
        break
    else:
        if( maior ):
            print("O seu chute foi maior que o número secreto")
        elif( menor ):
            print("O seu chute foi menor que o número secreto")
    rodada = rodada + 1

print("Game over, o número era", numero_secreto)