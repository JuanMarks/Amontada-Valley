sd = Sedan("Uti", 60000)
suv = SUV("Van", 80000)
conv = Conversivel("Conv", 100000)
sport = Sportivos("Ferrari", 150000)


nome = int(input("Ola primeiramente digite seu nome: \n aqui:  "))
dinheiro = int(input("Agora informe aqui sua conta: \n aqui:   "))

cliente = Usuario(nome, dinheiro)

print(f"Ola {cliente.nome}")
