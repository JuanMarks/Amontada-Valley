print("*******************************")
print("Bem vindo ao jogo da Advinhação")
print("*******************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um numero "))
    print("Voce digitou", chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Voce acertou")
    else:
        if(maior):
            print("Voce errou , numero maior que o numero secreto")
        elif(menor):
            print("Voce errou , numero menor que o numero secreto")
    rodada = rodada + 1

print("Fim de jogo")