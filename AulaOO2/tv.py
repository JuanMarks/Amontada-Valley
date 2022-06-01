class Televisor:
    def __init__(self, marca, tipo_de_tela, polegadas, preco, smarttv, entradas, tipo_de_som):
        self.marca = marca
        self.tipo_de_tela = tipo_de_tela
        self.polegadas = polegadas
        self.preco = preco
        self.smarttv = smarttv
        self.entradas = entradas
        self.tipos_de_som = tipo_de_som
        self.canal = 3
        self.volume = 20

    def ligando_tv(self):
        print("LIGANDO TELEVISOR")
    
    def desligar_tv(self):
        print("DESLIGANDO TELEVISOR")

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def aumentar_canal(self):
        self.canal += 1

    def diminuir_canal(self):
        self.canal -= 1
    
    def botao_internet(self):
        print("ENTRANDO NA INTERNET")

    def botao_netflix(self):
        print("ENTRANDO NA NETFLIX")

    def botao_menu(self):
        print("MENU")

    def mostrar_televisor(self):
        print(f"Este televisor é da marca {self.marca} e {self.tipo_de_tela} com {self.polegadas} de polegadas e se é SMART? {self.smarttv} as entradas são {self.entradas} com som {self.tipos_de_som} e seu preço é R${self.preco}")
        print(f"Volume:    {self.volume}")
        print(f"Canal:    {self.canal}")

    

televisao = Televisor('LG', 'LCD', 45, 2950, 'sim', 'HDMI, VGA e AV', 'Stereo')
televisao.ligando_tv()
televisao.mostrar_televisor()
televisao.aumentar_volume()
televisao.aumentar_volume()       
televisao.aumentar_volume()
televisao.mostrar_televisor()
televisao.diminuir_canal()
televisao.mostrar_televisor()
televisao.botao_internet()
televisao.botao_netflix()
televisao.botao_menu()
televisao.desligar_tv()