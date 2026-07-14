'''
senha = "123"
tentativa = ""
while(tentativa!=senha):
    tentativa = str(input('insira sua senha: '))
    if (tentativa!=senha):
        print("Erro!! Tente novamente")

print("Parabens, voce acertou a senha!!\n")
'''

import tkinter as tk

def verificaSenha():
    entrada = campo_senha.get()
    if entrada == '123':
        resultado.config(text="Conexão bem sucedida")
    else:
        resultado.config(text="Senha incorreta, tente novamente!!")

janela = tk.Tk()
janela.title("Verifica senha Wi-fi")
janela.geometry("500x500")

rotulo = tk.Label(janela, text="Digite a senha do wi-fi")
rotulo.pack()

campo_senha = tk.Entry(janela, show="")
campo_senha.pack()

botao = tk.Button(janela, text="Conectar", command=verificaSenha)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()