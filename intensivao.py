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
    global preco_total 
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
    global preco_total_bebida 
    preco_total_bebida = quant_bebida * preco_bebida

    print(f" Sabor: {nome_bebida} \n Tamanho: {tamanho_bebida} \n Preço total: {preco_bebida}")

def pedir_sobremesa():
    pedindo_sobremesa = int(input("Qual a sobremsa? \n (1) Sorvete \n (2) Pudim \n (3) Bolo \n"))
    if(pedindo_sobremesa == 1):
        nome_sobremesa = "Sorvete"
    elif(pedindo_sobremesa == 2):
        nome_sobremesa = "Pudim"
    elif(pedindo_sobremesa == 3):
        nome_sobremesa = "Bole"
    
    tamanho_sobremesa = int(input("Qual o tamanho da sobremsa? \n (1) Pequena \n (2) Media \n (3) Grande \n"))
    if(tamanho_sobremesa == 1):
        preco_sobremesa = 10
    elif(tamanho_sobremesa == 2):
        preco_sobremesa = 20
    elif(tamanho_sobremesa == 3):
        preco_sobremesa = 30
    
    quant_sobremesa = int(input("Qual a quantidade de sobremesas? \n (1) uma \n (2) duas \n (3) tres \n (N) Mais digite a quantidade \n "))
    global preco_total_sobremesa 
    preco_total_sobremesa = quant_sobremesa * preco_bebida

    print(f" Sabor: {nome_sobremesa} \n Tamanho: {tamanho_sobremesa} \n Preço total: {preco_sobreemsa}")

def conta():
    compra_total = preco_total + preco_total_bebida + preco_total_sobremesa
    return print(compra_total)

contador = False
preco_total = 0
preco_total_bebida = 0
preco_total_sobremesa = 0

while(contador == False):
    pedido = int(input("Voce vai querer pizza? \n (1) Sim \n (2) Nao \n"))
    if(pedido == 1):
        pedir_pizza()
    elif(pedido == 2):
        print("\n Proximo")
    pedido_bebida = int(input("Voce vai querer bebida? \n (1) Sim \n (2) Nao \n"))
    if(pedido_bebida == 1):
        pedir_bebida()
    elif(pedido_bebida == 2):
        print("\n Proximo")
    pedindo_sobremesa = int(input("Voce vai querer sobremesa? \n (1) Sim \n (2) Nao \n"))
    if(pedindo_sobremesa == 1):
        pedir_sobremesa()
    elif(pedindo_sobremesa == 2):
        print("\n Proximo")
    
    print("Valor total da sua compra é:  ")
    conta()
    contador = True





