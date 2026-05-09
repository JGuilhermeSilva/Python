import tkinter as tk

def adicionar_nome():
    nome = campo_nome.get()
    if nome != "":
        lista.insert(tk.END, f"Presente: {nome}")
        campo_nome.delete(0, tk.END) #deleta o que estiver escrito no campo

janela = tk.Tk()
janela.title("Chamada de turma")
#janela.geometry("500x500")

rotulo = tk.Label(janela, text="Digite o nome do aluno")
rotulo.pack()

campo_nome = tk.Entry(janela) #adicionar janela
campo_nome.pack()

botao = tk.Button(janela, text="Adicionar", command=adicionar_nome)
botao.pack()

lista = tk.Listbox(janela)
lista.pack()

janela.mainloop()