from comprador import Comprador
from lista_de_carros import *

sedan = Sedan("Sedan", 10000)
suv = SUV("SUV", 15000)
conv = Conversivel("Conversivel", 18000)
sport = Esportivos("Ferrari", 20000)

lista = [sedan, suv, conv, sport, suv, sedan]

print("BEM VINDO A LOJA AUTOMATICA DE CARROS \n")
nome = input("Agora digite seu nome:  ")
comprador = Comprador(nome, 50000)

print(f"Ola {comprador.nome} aqui esta a lista dos carros disponiveis para a venda")

i = 0
for carro in lista:
    i += 1
    print(f"({i}) {carro} \n")

resposta = int(input("Qual o carro voce vai comprar? \n Digite aqui sua resposta:  "))
comprador.comprar_carro(lista[resposta-1], lista)
        
