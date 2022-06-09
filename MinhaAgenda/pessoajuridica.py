from minhaagenda import MinhaAgenda
import re

class PessoaJuridica(MinhaAgenda):
    def __init__(self,nome, endereco, email, numero_contato, cnpj):
        super().__init__(nome, endereco, email, numero_contato)
        self._cnpj = cnpj
        self.verifica_cnpj()
    
    @property
    def cnpj(self):
        return self._cnpj
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj
    
    def verifica_cnpj(self):
        padrao = re.compile("[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[0-9]{2}")
        busca = padrao.search(self._cnpj)
        if busca:
            cnpj = busca.group()
            print(f"CNPJ nos conformes {cnpj}")
        else:
            print("CNPJ esta errado")