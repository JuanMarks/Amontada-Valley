def pedir_pizza():
    pedindo_pizza = int(input("Qual o sabor da Pizza? \n (1) Calabreza \n (2) Muzzarela \n (3) Portuguesa \n"))
    if(pedindo_pizza == 1):
        nome_pizza = "Calabresa"
    elif(pedindo_pizza == 2):
        nome_pizza = "Muzzarela"
    elif(pedindo_pizza == 3):
        nome_pizza = "Portuguesa"
    
    tamanho_pizza = int(input("Qual o tamanho da pizza? \n (1) Pequena \n (2) Media \n (3) Grande \n"))
    if(tamanho_pizza == 1):
        preco_pizza = 10
    elif(tamanho_pizza == 2):
        preco_pizza = 20
    elif(tamanho_pizza == 3):
        preco_pizza = 30
    
    quant_pizza = int(input("Qual a quantidade de pizzas? \n (1) uma \n (2) duas \n (3) tres \n (N) Mais digite a quantidade \n "))
    preco_total = quant_pizza * preco_pizza

    print(f" Sabor: {nome_pizza} \n Tamanho: {tamanho_pizza} \n Preço total: {preco_total}")


def pedir_bebida():
    pedindo_bebida = int(input("Qual a bebida? \n (1) Refri \n (2) Cerveja \n (3) Agua \n"))
    if(pedindo_bebida == 1):
        nome_bebida = "Refri"
    elif(pedindo_bebida == 2):
        nome_bebida = "Cerveja"
    elif(pedindo_bebida == 3):
        nome_bebida = "Agua"
    
    tamanho_bebida = int(input("Qual o tamanho da bebida? \n (1) Pequena \n (2) Media \n (3) Grande \n"))
    if(tamanho_bebida == 1):
        preco_bebida = 10
    elif(tamanho_bebida == 2):
        preco_bebida = 20
    elif(tamanho_bebida == 3):
        preco_bebida = 30
    
    quant_bebida = int(input("Qual a quantidade de bebidas? \n (1) uma \n (2) duas \n (3) tres \n (N) Mais digite a quantidade \n "))
    preco_total = quant_bebida * preco_bebida

    print(f" Sabor: {nome_bebida} \n Tamanho: {tamanho_bebida} \n Preço total: {preco_bebida}")



