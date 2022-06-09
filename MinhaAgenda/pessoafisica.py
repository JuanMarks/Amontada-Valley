from minhaagenda import MinhaAgenda
import re

class PessoaFisica(MinhaAgenda):
    def __init__(self,nome, endereco, email, numero_contato, data_de_aniversario, cpf):
        super().__init__(nome, endereco, email, numero_contato)
        self.data_de_aniversario = data_de_aniversario
        self._cpf = cpf
        self.verifica_cpf()
        self.verifica_email()

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf
    
    def verifica_cpf(self):
        padrao = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
        busca = padrao.search(self._cpf)
        if busca:
            cpf = busca.group()
            print(f"CPF nos conformes {cpf}")
        else:
            print("CPF esta errado")
    
    def verifica_email(self):
        padrao = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com+$)")
        busca = padrao.search(self.email)
        if busca:
            email = busca.group()
            print(f"Email nos conformes {email}")
        else:
            print("Voce digitou o email errado")
    
    def __str__(self):
        return f" \n Data de Aniversario: {self.data_de_aniversario} \n CPF: {self.cpf}"

pessoa = PessoaFisica("nome","endereco","juanpaulo77@gmail.com", "numero_contato", "data de aniversario", "061.351.563-30")
