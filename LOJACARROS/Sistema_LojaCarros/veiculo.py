class Veiculo:
    def __init__(self, modelo, preco):
        self._modelo = modelo
        self._preco = preco
        self.vezes_que_foi_oficina = 0
        self.test_drive = False
        self.manuntencao = False
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def preco(self):
        return self._preco

    def verifica_oficina(self):
        if self.manuntencao == False:
            self.manuntencao = True
            self.vezes_que_foi_oficina += 1
            print("Carro foi pra manutenção")
        elif self.manuntencao == True:
            self.manuntencao = False
            print("Carro voltou da manuntenção")
    
    def testdrive(self):
        self.test_drive = True
    
    def __str__(self):
        return f"Modelo: {self._modelo} \n Status: {self.vezes_que_foi_oficina} \n Manuntenção: {self.manuntencao} \n"