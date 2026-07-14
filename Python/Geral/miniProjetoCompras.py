'''programa que calcula valor de uma lista de compras
de supermercado'''

import tkinter as tk
from tkinter import ttk

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
        #integrando a função de calcular valor para atualizar
        #automaticamente ao inserir produto na lista
        calcularTotal()

def calcularTotal():
    total = 0
    for produto in compras:
        total += produto["quantidade"] * produto["valor"]
        somaTotal.config(text=f"Valor total da compra: R${total:.2f}")

def forma_pagamento():
    pagamento = campo_pagamento.get()
    if pagamento.lower() == 'cartao':
        escolhaFormaPagamento.config(text="Pagamento escolhido: Cartão", bg='green')
    elif pagamento.lower() == 'pix':
        escolhaFormaPagamento.config(text="Pagamento escolhido: Pix", bg='green')
    elif pagamento.lower() == 'especie':
        escolhaFormaPagamento.config(text="Pagamento escolhido: Em espécie", bg='green')
    else:
        escolhaFormaPagamento.config(text="Escolha uma forma de pagamento válida!!", bg='red')

#iniciando interface grafica
janela = tk.Tk()
janela.title("Projeto lista de compras")
janela.geometry("600x800")
janela.config(bg="grey")


rotulo = tk.Label(janela, text="Lista de compras", font=("Arial" ,13, "bold"))
rotulo.pack()

rotulo_nome = tk.Label(janela, text="Nome do produto:").pack()
campo_nome = tk.Entry(janela, text="")
campo_nome.pack()

rotulo_quantidade = tk.Label(janela, text="Quantidade do produto:").pack()
campo_quantidade = tk.Entry(janela, text="")
campo_quantidade.pack()

rotulo_valor = tk.Label(janela, text="Valor do produto:").pack()
campo_valor = tk.Entry(janela, text="")
campo_valor.pack()

#janela.bind('<Return>', adicionarProduto)
botao = ttk.Button(janela, text="Adicionar", command=adicionarProduto)
botao.pack()

#Lista visual para mostrar produtos inseridos
lista = tk.Listbox(janela)
lista.pack()

#criando botao para mostrar valor total da compra
#somaTotal = tk.Button(janela, text='Calcular total:', command=calcularTotal)
#somaTotal.pack()

#mostra valor total da compra
somaTotal = tk.Label(janela, text="", foreground="red")
somaTotal.pack()

tk.Label(janela, text="Digite uma forma de pagamento('Pix', 'Cartão', ou 'Em espécie')").pack()

#recebe uma entrada da forma de pagamento
campo_pagamento = tk.Entry(janela, text='')
campo_pagamento.pack()

#adiciona a forma de pagamento da compra
botao_pagamento = ttk.Button(janela, text="Adicionar Forma", command=forma_pagamento)
botao_pagamento.pack()

#retorna ao usuario se a forma de pagamento é valida
escolhaFormaPagamento = tk.Label(janela, text="", foreground="black")
escolhaFormaPagamento.pack()

janela.mainloop()