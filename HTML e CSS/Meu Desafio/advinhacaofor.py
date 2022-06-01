import random

def jogar_advinhacao():
    numero_secreto = random.randrange(1, 100)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil   (2) Medio    (3) Dificil")
    nivel = int(input("Defina um nivel: "))

    if(nivel == 1): total_tentativas = 20
    elif(nivel == 2): total_tentativas = 10
    else: total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite um numero "))
        print("Voce digitou", chute)

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou , numero maior que o numero secreto")
            elif(menor):
                print("Voce errou , numero menor que o numero secreto")
            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos - pontosPerdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar_advinhacao()