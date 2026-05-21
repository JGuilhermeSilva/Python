'''num = int(input("insira um numero: "))
verifica = num%2
if (verifica == 1):
    print("impar")
else:
    print("par")'''

import tkinter as tk

def verificaNumero():
    entrada = int(campo_entrada.get())

    if (entrada%2 == 0):
        resultado.config(text=str('O número informado é PAR!'))
    elif (entrada%2 == 1):
        resultado.config(text=str('O número informado é IMPAR!'))
    '''elif type(entrada)!=type(int):
        resultado.config(text=str('Informe um valor válido!!!'))'''
    campo_entrada.delete(0, tk.END)


janela = tk.Tk()
janela.title("Par ou impar?")
janela.geometry("300x300")

rotulo = tk.Label(janela, text="Insira um número")
rotulo.pack()

campo_entrada = tk.Entry(janela, text="")
campo_entrada.pack()

botao = tk.Button(janela, text="Inserir", command=verificaNumero)
botao.pack()
#janela.bind('<Return>', verificaNumero)

resultado = tk.Label(janela, text='')
resultado.pack()

janela.mainloop()
    