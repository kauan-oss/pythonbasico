import random
#Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print("\nEscolha o nível: ")
    print("1 -- Fácil (10 tentativas)")
    print("2 -- Médio (5 tentativas)")
    print("3 -- Difícil (3 tentativas)")

    while True:
        nivel_str = input("Digite apenas números (1, 2, 3):")
        if not nivel_str.isdigit():
            print(VERMELHO+"Digite apenas número!"+ RESET)
            continue
        nivel = int(nivel_str)
        if nivel == 1:
            return 10
        elif nivel == 2:
            return 5
        elif nivel == 3:
            return 3
        else:
            print(AMARELO+"Escolha apenas 1,2 ou 3"+RESET)

def jogar():

    print(AZUL+'*************************'+RESET)
    print(AZUL+'** Jogo da adivinhação **'+RESET)
    print(AZUL+'*************************'+RESET)
    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,101)
    pontos = 100
    historico = []

    for rodada in range(1, total_tentativas + 1 ):
        print(f"\nTentativa {rodada} de {total_tentativas}")
        
        chute_str = input( "Digite um número entre 1 e 100:")

        if not chute_str.isdigit:
            print(VERMELHO+"Dígite um número entre 1 e 100:"+RESET)
            continue 

        chute = int(chute_str)

        if(chute <1 or chute > 100):
            print(AMARELO+"Você deve digitar números entre 1 e 100!"+RESET)
            continue
        historico.append(chute)

        if chute == numero_secreto:
            print(VERDE+"\nVocê acertou!!"+RESET)
            print(VERDE+f"\nSua pontuação foi: {pontos} pontos"+RESET)
            break
        else:
            pontos -= 20
            if chute > numero_secreto:
                print(VERMELHO+"\nO número secreto é menor!!"+RESET)
            else:
                print(VERMELHO+"\nO número secreto é maior!!"+RESET)
    else:
        print(VERMELHO+f"\nVocê perdeu! o número secreto é {numero_secreto}"+RESET)
    print(AZUL+"\nHistórico de tentativas: "+RESET,historico)
    print(AZUL+"Fim de jogo "+RESET)

while True:
    jogar()
    repetir = input("\nDeseja jogar novamente? (s/n)").lower()

    if repetir != "s":
        print(AZUL+"\nObrigado por jogar!"+RESET)
        break