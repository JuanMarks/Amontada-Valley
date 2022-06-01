import forca
import advinhacaofor

print("*******************************")
print("******Escolha seu Jogo*********")
print("*******************************")

print("(1) Jogo da Forca      (2) Jogo da Advinhação")

jogo = int(input("Qual o jogo?:  "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando Advinhação")
    advinhacaofor.jogar_advinhacao()
    