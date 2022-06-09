from minhaagenda import MinhaAgenda
import re

class PessoaFisica(MinhaAgenda):
    def __init__(self,nome, endereco, email, numero_contato, data_de_aniversario, cpf):
        super().__init__(nome, endereco, email, numero_contato)
        self.data_de_aniversario = data_de_aniversario
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf
    
    def __str__(self):
        return f" \n Data de Aniversario: {self.data_de_aniversario} \n CPF: {self.cpf}"

pessoa = PessoaFisica("nome","endereco","juanpaulo77@gmail.com", "numero_contato", "data de aniversario", "061.351.563-30")
