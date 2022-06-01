from conta import Conta

gui = Conta(15)
gui.deposita(500)

dani = Conta(45689)
dani.deposita(1000)

contas = [gui, dani]

for conta in contas:
    print(conta)