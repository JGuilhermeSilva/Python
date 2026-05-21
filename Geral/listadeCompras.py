'''
item = ''
lista = []
while (item!='fim'):
       item = str(input("Insira seu produto | Ou 'fim' para encerrar: "))
       if(item!='fim'):
           lista.append(item)
print("lista de compras concluida!!")
print(lista)'''

import tkinter as tk

def adicionaItem():
    item = campo_item.get()
    if item!="":
        lista.insert(tk.END, item)
        campo_item.delete(0, tk.END)

janela = tk.Tk()
janela.title("Lista de compras")
janela.geometry("300x150")

rotulo = tk.Label(janela, text="Adicione um item: ")
rotulo.pack()

campo_item = tk.Entry(janela, text="")
campo_item.pack()

botao = tk.Button(janela, text="Adicionar", command=adicionaItem)
botao.pack()

lista = tk.Listbox(janela)
lista.pack()

janela.mainloop()