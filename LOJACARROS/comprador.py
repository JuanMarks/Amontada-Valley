from lista_de_carros import *

class Comprador:
    def __init__(self, nome, dinheiro, carro):
        self.nome = nome
        self._dinheiro = dinheiro
        self.carro = carro
    
    @property
    def dinheiro(self):
        return self._dinheiro
    
    def verifica_carro(self, lista):
        if self.carro in lista:
            print("Esse é o carro que eu quero \n")
        else:
            print("Nao tem o carro que eu quero \n")
    
    def comprar_carro(self, lista):
        if self._dinheiro >= self.carro.preco:
            self._dinheiro -= self.carro.preco
            print(f"Consegui comprar o carro e sobrou {self._dinheiro}")
            if self.carro in lista:
                lista.remove(self.carro)
            else:
                print("Nao tem o carro na lista")
        else:
            print("Nao tem dinheiro o suficiente para comprar o carro")
        