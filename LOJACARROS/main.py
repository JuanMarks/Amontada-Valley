from comprador import Comprador
from lista_de_carros import *
from vendedor import Vendedor

sedan = Sedan("coisa", 10000)
suv = SUV("SUV", 15000)
conv = Conversivel("conversivel", 18000)
sport = Esportivos("ferrari", 20000)

lista = [sedan, suv, conv, sport]

sedan.verifica_oficina()
sedan.verifica_oficina()

print(sedan)

comprador1 = Comprador("Joao", 20000, sedan)

vendedor = Vendedor("Raimundo")
vendedor.atribuir_comprador(comprador1)

vendedor.vender(lista)

print(lista)