import random
print('*************************')
print('** Jogo da adivinhação **')
print('*************************')

dificuldade_escolhida = print ("1-Fácil, 2-Médio, 3-Díficil")
escolha = input("Esolha a dificuldade 1, 2 e 3")

escolha == 1
print(f"Você vai jogar tranquilo")

escolha == 2
print(f"Gosta de um pouco de dificuldade")

escolha == 3
print(f"Gosta de um jogo complexo")

numero_secreto = random.randrange( 1,101 )
total_tentativas = 3

for rodada in range(1, total_tentativas +1 ):
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    
    chute_str = input( "Digite o seu número:")
    print( "Seu número é", chute_str )
    chute = int(chute_str)

    if(chute <1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if( acertou ):
        print("Você acertou")
        break
    else:
        if( maior ):
            print("O seu chute foi maior que o número secreto tente no próximo o número um pouco menor")
        elif( menor ):
            print("O seu chute foi menor que o número secreto tente no próximo o número um pouco maior")

print("Game over, o número era", numero_secreto)