from racao import Racao

class Equinos(Racao):
    def __init__(self, marca, sabor, preco, preco_kg):
        super().__init__(marca, sabor, preco, preco_kg)

class Caprinos(Racao):
    def __init__(self, marca, sabor, preco, preco_kg):
        super().__init__(marca, sabor, preco, preco_kg)

class Caninos(Racao):
    def __init__(self, marca, sabor, preco, preco_kg):
        super().__init__(marca, sabor, preco, preco_kg)

class Felinos(Racao):
    def __init__(self, marca, sabor, preco, preco_kg):
        super().__init__(marca, sabor, preco, preco_kg)