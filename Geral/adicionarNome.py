import tkinter as tk
from tkinter import ttk

def adicionar_nome(event = None):
    nome = campo_nome.get()
    if nome != "":
        lista.insert(tk.END, f"Presente: {nome}")
        campo_nome.delete(0, tk.END) #deleta o que estiver escrito no campo

janela = tk.Tk()
janela.title("Chamada de turma")
#janela.geometry("500x500")
#
janela.minsize(300, 300)
janela.maxsize(500, 500)
janela.resizable(True, True)
#
rotulo = ttk.Label(janela, text="Digite o nome do aluno")
rotulo.pack()

campo_nome = tk.Entry(janela) #adicionar janela
campo_nome.pack()

#usa metodo bind para tambem reconhecer a tecla "ENTER" como ativadora da funcao
janela.bind('<Return>', adicionar_nome)
botao = ttk.Button(janela, text="Adicionar", command=adicionar_nome)
botao.pack()


lista = tk.Listbox(janela)
lista.pack()


estilo = ttk.Style(janela)
#estilizar todos os botoes:
#primeiro saber o nome do tipo de elemento:

print(botao.winfo_class()) #como o BOTAO esta definido com ttk irá aparecer TButton,caso seja definido com tk.Button irá aparecer Button(náo é editavel)

#Alterar o estilo pata todos os componentes TButton:
#Altera Fonte e Estilo ("TButton", font=("NomeDaFonte", Tamanho, "Estilo"), foreground="Cor do texto")
estilo.configure('TButton', font=("Arial", 10, "italic"), foreground='blue')
#faz a mesma coisa com as Label's da janela
estilo.configure('TLabel', font=("Hermetic", 10, "italic"), foreground='blue')

janela.mainloop()