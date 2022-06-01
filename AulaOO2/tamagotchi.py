class Bichinho:
    def __init__(self, nome):
        self.__nome = nome
        self.__fome = 0
        self.__saude = 100
        self.__humor = 100
        self.__idade = 1
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade

    def alimentar(self):
        self.__fome -= 10

    def medicar(self):
        self.__saude += 10

    def humor(self):
        self.__fome + self.__saude / 2

    

        