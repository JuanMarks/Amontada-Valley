class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self.likes += 1

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Duração: {self.duracao}min  Likes: {self._likes}'

        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Temporadas: {self.temporadas}  Likes: {self._likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def __len__(self):
        return len(self._programas)


        
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
got = Serie('game of thronnes', 2012, 8)

listinha = [vingadores, got, tmep, demolidor]
fim_de_semana = Playlist('Fim de Semana', listinha)

for programa in fim_de_semana:
    print(programa)
        