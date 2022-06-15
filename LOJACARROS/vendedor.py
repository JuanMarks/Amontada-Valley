from comprador import Comprador

class Vendedor:
    def __init__(self, nome):
        self.nome = nome
    
    def atribuir_comprador(self, comprador):
        self.comprador = comprador
    
    def definir_carro(self, carro):
        self.carro = carro

    def vender(self, lista):
        self.comprador.verifica_carro(lista)
        self.comprador.comprar_carro(lista)