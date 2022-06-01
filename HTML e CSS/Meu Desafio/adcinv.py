from tkinter import *
from webbrowser import get
from tkinter import ttk
import openpyxl

book = openpyxl.Workbook()
book.create_sheet('produtos')
produtos_page = book['produtos']
produtos_page.append(['ID', 'PRODUTOS','PREÇO'])

'''def save_produtos():
    numeroid = int()
    produto_nome_entry = str()
    produto_preco_entry = float()
    produtos_page.append([numeroid, produto_nome_entry,produto_preco_entry])
    book.save('Inventario1.xlsx')'''

def janela_inv():
    janela = Tk()
    janela.title("INVENTARIO")
    janela.geometry("500x700")

    texto_orientacao = Label(janela, text="INVENTARIO",font="30", pady=40)
    texto_orientacao.grid(column=1, row=0)

    id = Label(janela, text="Numero de Identificação", font="12", pady=20)
    id.grid(column=0, row=1)
    numeroid = Entry(janela, font="12")
    numeroid.grid(column=1, row=1)
    

    produto_nome = Label(janela, text="Nome do Produto", font="12", pady=20)
    produto_nome.grid(column=0, row=2)
    produto_nome_entry = Entry(janela, font="12")
    produto_nome_entry.grid(column=1, row=2)

    produto_preco = Label(janela, text="Preço do Produto", font="12", pady=20)
    produto_preco.grid(column=0, row=3)
    produto_preco_entry = Entry(janela, font="12")
    produto_preco_entry.grid(column=1, row=3)

    produtos_page.append([numeroid, produto_nome_entry, produto_preco_entry])

    botao = Button(janela, text="Adcionar no Inventario",command=book.save('Inventario1.xlsx'), bg="blue", font="20")
    botao.grid(column=1, row=4, padx=20, pady=20)

    janela.mainloop()

janela_inv()


