import openpyxl

book = openpyxl.Workbook()
book.create_sheet('produtos')
produtos_page = book['produtos']
produtos_page.append(['ID', 'PRODUTOS','PREÇO'])

contador = False

while(contador == False):
    numeroid = int(input("Digite o numero do produto: "))
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    produtos_page.append([numeroid, nome_produto, preco_produto])

    print("Voce quer adcionar mais algum produto??")
    print("(1) Sim    (2)  Não")
    resposta = int(input("Digite aqui sua resposta:  "))

    if(resposta == 1):
        numeroid = int(input("Digite o numero do produto: "))
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        produtos_page.append([numeroid, nome_produto, preco_produto])

        print("Voce quer adcionar mais algum produto??")
        print("(1) Sim    (2)  Não")
        resposta = int(input("Digite aqui sua resposta:  "))
    else:
        contador = True

book.save('Inventario.xlsx')