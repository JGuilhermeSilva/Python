import tkinter as tk
from tkinter import ttk

def mostrar_selecao():
    # Obtém o índice do item selecionado
    selecionado = lista.curselection()
    if selecionado:
        item = lista.get(selecionado)
        label_resultado.config(text=f"Selecionado: {item}")

# Configuração da janela principal
app = tk.Tk()
app.title("Exemplo de Lista")
app.geometry("300x250")

# Criando o widget Listbox
lista = tk.Listbox(app, selectmode=tk.SINGLE)
lista.pack(pady=10)

# Adicionando itens à lista
itens = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in itens:
    lista.insert(tk.END, item)

# Botão para ação
btn = tk.Button(app, text="Imprimir Seleção", command=mostrar_selecao)
btn.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(app, text="")
label_resultado.pack(pady=5)

#imprime lista suspensa 
'''combo = ttk.Combobox(app, values=["Opção 1", "Opção 2", "Opção 3"])
combo.pack()'''

app.mainloop()
