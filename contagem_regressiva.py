'''
contador = 5

while(contador > 0):
    print(contador)
    contador-=1;
print('acabou')
'''

import tkinter as tk

contador = 10

def iniciarContagem():
    global contador

    if contador > 0:
        resultado.config(text=str(contador))
        contador -= 1
        janela.after(1000, iniciarContagem)
    else:
        resultado.config(text=str("Acabou-se o mundo"))

janela = tk.Tk()
janela.title("Contagem regressiva de 10 a 0")
janela.geometry("300x300")
'''
rotulo = tk.Label(janela, text="Começando")
rotulo.pack()
'''
resultado = tk.Label(janela, text="")
resultado.pack()

botao = tk.Button(janela, text="Comecar", command=iniciarContagem)
botao.pack()

janela.mainloop()