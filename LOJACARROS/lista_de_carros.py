from veiculo import Veiculo
class Sedan(Veiculo):
    def __init__(self, modelo, preco):
        super().__init__(modelo, preco)

class SUV(Veiculo):
    def __init__(self, modelo, preco):
        super().__init__(modelo, preco)

class Conversivel(Veiculo):
    def __init__(self, modelo, preco):
        super().__init__(modelo, preco)

class Esportivos(Veiculo):
    def __init__(self, modelo, preco):
        super().__init__(modelo, preco)