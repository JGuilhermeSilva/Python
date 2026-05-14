import tkinter as tk


def calculadora():
    if (escolha=="soma" or escolha=="+"):
        soma = num1 + num2
        resultado.config(text=f"Soma de {num1}+{num2} = {soma}")

    elif (escolha=="subtracao" or escolha=="-"):
        subtracao = num1-num2
        resultado.config(text=f"Subtracao de {num1}-{num2} = {subtracao}")

    elif (escolha=="multiplicacao" or escolha=="*"):
        multiplicacao = num1 * num2
        resultado.config(text=f"Multiplicacao de {num1}x{num2} = {multiplicacao}")

    elif (escolha=="divisao" or escolha=="/"):
        if num2 != 0:
            divisao = num1/num2
            resultado.config(text=f"Divisão de {num1}/{num2} = {divisao}\n")
        else:
            resultado.config(text=f"ERRO: Não é possivel dividir por 0!!!")
    
    else:
        resultado.config(text=f"Nao entendi, recomece o programa")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x500")   

tk.Label(janela, text="Calculadora Python/Tkinter").pack()

tk.Label(janela, text="Inserir valor 1:").pack()
num1 = tk.Entry(janela)
num1.pack()

tk.Label(janela, text="Inserir valor 2:").pack()
num2 = tk.Entry(janela)
num2.pack()

rotuloEscolha = tk.Label(janela, text="Insira o tipo de operação:")
rotuloEscolha.pack()
escolha = tk.Entry(janela, text="")
escolha.pack()

botao = tk.Button(janela, text="Calcular", command=calculadora)
botao.pack()

resultado = tk.Label(janela, text='')
resultado.pack()


janela.mainloop()