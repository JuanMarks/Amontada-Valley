from socket import NI_NUMERICHOST
from conta import Conta
def criar_conta():
    numero = input("Digite o numero da conta:  ")
    titular = input("Digite o nome do titular da conta:  ")
    saldo = input("saldo:  ")
    limite = 1000
    conta = Conta(numero, titular, saldo, limite)
    return conta



criar_conta()



