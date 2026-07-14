'''
peso = 64.00
altura = 1.75
imc = (peso/(altura*altura))
print(f"Seu IMC é: {imc:.2f}")

if(imc < 18.5):
    print('abaixo do peso')
elif(imc >=18.5 and imc <= 24.9):
    print("normal")
elif(imc >=25 and imc <= 29.9):
    print("sobrepeso")
elif(imc >=30):
    print("obeso")
'''

import tkinter as tk

def calculaImc():
    peso = float(campo_peso.get())
    altura = float(campo_altura.get())
    imc = float(peso/(altura ** 2)) #peso/altura ao quadrado
    '''    if peso!=""
        peso.insert(0, text="Peso: ")
    if peso=="Peso: ":
        campo_peso.delete(0, tk.END)
'''

    if(imc < 18.5):
        resultado.config(text=str("abaixo do peso"))
    elif(imc >=18.5 and imc <= 24.9):
        resultado.config(text=str("normal"))
    elif(imc >=25 and imc <= 29.9):
        resultado.config(text=str("sobrepeso"))
    elif(imc >=30):
        resultado.config(text=str("obeso"))

janela = tk.Tk()
janela.title("Calculadora IMC")
janela.geometry("500x500")

campo_peso = tk.Entry(janela, text='')
campo_peso.pack()

campo_altura = tk.Entry(janela, text='')
campo_altura.pack()

resultado = tk.Label(janela, text='')
resultado.pack()

botao = tk.Button(janela, text="Calcular imc", command=calculaImc)
botao.pack()

janela.mainloop()