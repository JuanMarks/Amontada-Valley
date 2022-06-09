from tipos_de_racao import *

class Vender:
    def __init__(self,cliente,lista):
        self.cliente = cliente
        self.lista = lista

    def vender_racao(self):
        print(f"Ola {self.cliente.nome} que tipo de ração voce gostaria de comprar?")
        resposta = int(input("(1) Equinos \n (2) Caprinos \n (3) Caninos (4) Felinos \n Sua resposta aqui:   "))
        
        if resposta == 1:
            equino = Equinos()
            
            print("Quantos quilos de ração voce gostaria de comprar?")
            kilos = int(input("(1) 5kg \n (2) 10kg \n (3) 20kg \n (4) Saco de 30kg \n Digite sua resposta aqui: "))
            
            if kilos == 1:
                racao = 5 * equino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {equino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 2:
                racao = 10 * equino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {equino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 3:
                racao = 20 * equino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {equino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 4:
                racao = equino.preco
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {equino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
        
        if resposta == 2:
            caprino = Caprinos()
            
            print("Quantos quilos de ração voce gostaria de comprar?")
            kilos = int(input("(1) 5kg \n (2) 10kg \n (3) 20kg \n (4) Saco de 30kg \n Digite sua resposta aqui: "))
            
            if kilos == 1:
                racao = 5 * caprino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {caprino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 2:
                racao = 10 * caprino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {caprino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 3:
                racao = 20 * caprino.preco_kg
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {caprino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
            
            if kilos == 4:
                racao = caprino.preco
                if self.cliente.dinheiro >= racao:
                    print(f"Voce comprou 5kg dessa ração: {caprino.marca}")
                else:
                    print("Voce nao tem dinheiro o suficiente para comprar essa ração")
        
