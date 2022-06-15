from lista_de_carros import *

class Comprador:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self._dinheiro = dinheiro
        
    
    @property
    def dinheiro(self):
        return self._dinheiro
    
    def verifica_carro(self, lista):
        if self.carro in lista:
            print("Esse é o carro que eu quero \n")
        else:
            print("Nao tem o carro que eu quero \n")
    
    def comprar_carro(self, carro, lista):
        self.carro = carro
        if self._dinheiro >= self.carro.preco:
            self._dinheiro -= self.carro.preco
            print(f"Ola {self.nome} voce acaba de adquirir o carro \n \n {self.carro} \n seu saldo ficou: {self._dinheiro} \n \n Obrigado e volte sempre")
            if self.carro in lista:
                lista.remove(self.carro)
            else:
                print("Nao tem o carro na lista")
        else:
            print("Nao tem dinheiro o suficiente para comprar o carro")
    
    def __str__(self):
        return f"Comprador: {self.nome} \n Dinheiro: {self._dinheiro}"
        