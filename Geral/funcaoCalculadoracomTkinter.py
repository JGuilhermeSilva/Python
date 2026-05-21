import tkinter as tk


def calculadora(event=None):
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    escolha = escolhaOP.get()
    if (escolha=="soma" or escolha=="+"):
        soma = num1 + num2
        resultado.config(text=f"Soma de {num1}+{num2} = {soma:.2f}")

    elif (escolha=="subtracao" or escolha=="-"):
        subtracao = num1-num2
        resultado.config(text=f"Subtracao de {num1}-{num2} = {subtracao:.2f}")

    elif (escolha=="multiplicacao" or escolha=="*"):
        multiplicacao = num1 * num2
        resultado.config(text=f"Multiplicacao de {num1}x{num2} = {multiplicacao:.2f}")

    elif (escolha=="divisao" or escolha=="/"):
        if num2 != 0:
            divisao = num1/num2
            resultado.config(text=f"Divisão de {num1}/{num2} = {divisao:.2f}\n")
        else:
            resultado.config(text=f"ERRO: Não é possivel dividir por 0!!!")
    
    else:
        resultado.config(text=f"Nao entendi, recomece o programa")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x500")   

tk.Label(janela, text="Calculadora Python/Tkinter").pack()

tk.Label(janela, text="Inserir valor 1:").pack()
entrada1 = tk.Entry(janela, text="")
entrada1.pack()

tk.Label(janela, text="Inserir valor 2:").pack()
entrada2 = tk.Entry(janela, text="")
entrada2.pack()

tk.Label(janela, text="Insira o tipo de operação:").pack()
escolhaOP = tk.Entry(janela, text="")
janela.bind('<Return>', calculadora)
escolhaOP.pack()


botao = tk.Button(janela, text="Calcular", command=calculadora)
botao.pack()

resultado = tk.Label(janela, text='')
resultado.pack()


janela.mainloop()