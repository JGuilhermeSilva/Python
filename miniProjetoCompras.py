'''programa que calcula valor de uma lista de compras
de supermercado

'''

import tkinter as tk
#from tkinter import ttk

#lista para armazenar os produtos
compras = []

#funcao para adicionar um produto
def adicionarProduto():
    nome = campo_nome.get()
    quantidade = campo_quantidade.get()
    valor = campo_valor.get()

    if nome!='' and quantidade!='' and valor!='':
        produto = {
            "nome": nome,
            "quantidade": int(quantidade),
            "valor": float(valor)
        }
        compras.append(produto)
        lista.insert(tk.END, f"{nome} - {quantidade} X R${valor}")
        campo_nome.delete(0, tk.END)
        campo_quantidade.delete(0, tk.END)
        campo_valor.delete(0, tk.END)

def calcularTotal():
    total = 0
    for produto in compras:
        total += produto["quantidade"] * produto["valor"]
        resultado.config(text=f"Valor Total da compra: R${total:.2f}")

def forma_pagamento():
    pagamento = campo_pagamento.get()
    if pagamento.lower() == 'cartao':
        resultado.config(text="Pagamento escolhido: Cartão")
    elif pagamento.lower() == 'pix':
        resultado.config(text="Pagamento escolhido: Pix")
    elif pagamento.lower() == 'especie':
        resultado.config(text="Pagamento escolhido: Em espécie")
    else:
        resultado.config(text="Escolha uma forma de pagamento válida!!")


janela = tk.Tk()
janela.title("Projeto lista de compras")
janela.geometry("500x500")

rotulo = tk.Label(janela, text="Lista de compras")
rotulo.pack()

campo_nome = tk.Entry(janela, text="")
campo_nome.pack()

campo_quantidade = tk.Entry(janela, text="")
campo_quantidade.pack()

campo_valor = tk.Entry(janela, text="")
campo_valor.pack()

janela.bind('<Return>', adicionarProduto)
botao = tk.Button(janela, text="Adicionar", command=adicionarProduto)
botao.pack()

lista = tk.Listbox(janela)
lista.pack()

botao2 = tk.Button(janela, text="Mostrar valor", command=calcularTotal)
botao2.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()