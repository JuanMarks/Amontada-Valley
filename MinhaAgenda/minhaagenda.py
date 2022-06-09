import re

class MinhaAgenda:
    def __init__(self, nome, endereco, email, numero_contato):
        self._nome = nome
        self.endereco = endereco
        self.email = email
        self.numero_contato = numero_contato
        self.verifica_email()
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome
    
    def verifica_email(self):
        padrao = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com+$)")
        busca = padrao.search(self.email)
        if busca:
            email = busca.group()
            print(f"Email nos conformes {email}")
        else:
            print("Voce digitou o email errado")
    
    def __str__(self):
        return f" Nome: {self._nome} \n Endereço: {self.endereco} \n Email: {self.email} \n Numero de Contato: {self.numero_contato}"
