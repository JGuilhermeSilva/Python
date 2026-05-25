import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.title("Teste com customTkinter")
janela.geometry("500x300")

def clique(event = None):
    EntradaEmail = campoEntradaEmail.get()
    entradaSenha = campoEntradaSenha.get()
    if entradaSenha!="":
        if EntradaEmail == "aaa" and entradaSenha == "123":
            resultado.configure(text="Usuario Logado com sucesso", text_color="green")
        else:
            resultado.configure(text="Senha Incorreta", text_color="red")
    else:
        resultado.configure(text="Insira as informações!!", text_color="red")
titulo = customtkinter.CTkLabel(janela, text="Tela de Login:").pack()


campoEntradaEmail = customtkinter.CTkEntry(janela, placeholder_text="Email")
campoEntradaEmail.pack(padx=10, pady=10)

campoEntradaSenha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
campoEntradaSenha.pack(padx=10, pady=10)

janela.bind('<Return>', clique)
botao = customtkinter.CTkButton(janela, text="Tentar", command=clique)
botao.pack()

resultado = customtkinter.CTkLabel(janela, text="")
resultado.pack(padx=10, pady=10)
janela.mainloop()