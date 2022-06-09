class Racao:
    def __init__(self, marca, sabor, preco, preco_kg):
        self.marca = marca
        self.sabor = sabor 
        self._preco = preco
        self._preco_kg = preco_kg

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco
    
    @property
    def preco_kg(self):
        return self._preco_kg
    @preco_kg.setter
    def preco_kg(self, novo_preco_kg):
        self._preco_kg = novo_preco_kg

    