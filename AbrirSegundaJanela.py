'''import tkinter as tk
#teste de alteracao 2
janela = tk.Tk()

janela.title("Página Principal")
janela.geometry("500x400+200+100")
janela.config(bg="lightgreen") #mudar cor da janela

'''
#janela.maxsize(800, 600) #definir o tamanho máximo (lar x alt) que uma janela pode ser redimensionada
#janela.minsize(300, 200) #definir o tamanho mínimo (lar x alt) que uma janela pode ser redimensionada
#janela.resizable(True, False) #permite que redimensione a largura da janela, mas bloqueia o redimensionamento vertical (altura)
#janela.state('zoomed') #deixa o estado inicial da janela como tela inteira
#janela.attributes('-alpha', 0.6) #deixa a transparencia da janela em 60%
'''

janela.iconbitmap('logo.ico') #muda o icone padrao

janela.mainloop()

'''
import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segunda janela")
    segunda_janela.config(bg='pink')

    #tamanho da janela
    largura_janela = 300
    altura_janela = 200

    #obter dimensoes da tela do monitor
    largura_tela_monitor = segunda_janela.winfo_screenwidth()
    altura_tela_monitor = segunda_janela.winfo_screenheight()

    #calcular as coordenadas para centralizar a janela 2 na tela
    x = (largura_tela_monitor - largura_janela) // 2
    y = (altura_tela_monitor - altura_janela) // 2

    #definir geometria da janela 2
    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

#criar janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Janela Principal")
janelaPrincipal.config(bg="blue")
janelaPrincipal.geometry("600x500")

#cria um evento lambda que todo clique com o botao esquerdo do mouse chama a funcao abrir_segunda_janela()
janelaPrincipal.bind("<Button-1>", lambda event: abrir_segunda_janela())

janelaPrincipal.mainloop()