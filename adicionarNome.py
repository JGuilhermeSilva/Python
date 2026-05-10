import tkinter as tk

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
janela.resizable(True, False)
#
rotulo = tk.Label(janela, text="Digite o nome do aluno")
rotulo.pack()

campo_nome = tk.Entry(janela) #adicionar janela
campo_nome.pack()

janela.bind('<Return>', adicionar_nome)
botao = tk.Button(janela,event=None, text="Adicionar", command=adicionar_nome)
botao.pack()


lista = tk.Listbox(janela)
lista.pack()


janela.mainloop()