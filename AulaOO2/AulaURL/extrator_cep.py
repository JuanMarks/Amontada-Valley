import re
endereco = "Rua Joaquim Tome Rodrigues, casa 760-2, Amontada, Ceara, CE, 62540-000"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)