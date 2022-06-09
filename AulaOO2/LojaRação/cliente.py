class Cliente:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self._dinheiro = dinheiro
    
    @property
    def dinheiro(self):
        return self._dinheiro