'''Este script vai abrir o Bloco de Notas, digitar um texto (simulando a descrição
 que você quer colar) e interagir com o menu superior.'''

from pywinauto import Application
import pywinauto
import time

# 1. Abre o programa (ou conecta a um que já está aberto usando .connect())
app = Application(backend="uia").start("notepad.exe")

# 2. Seleciona a janela principal do Bloco de Notas
# O pywinauto consegue achar a janela pelo título dela (ex: "Sem título - Bloco de Notas")
janela = app.window(title_re="* Sem título - Bloco de notas*")

# 3. Espera a janela ficar pronta para receber comandos
janela.wait("visible", timeout=3)

# 4. Localiza o campo de texto principal e digita algo
# No Bloco de Notas do Windows 11, o campo de texto se chama "Documento RichEdit" ou "Editor"
campo_texto = janela.child_window(auto_id="TextEditor", control_type="Dialog")
campo_texto.type_keys("Inserindo o número do item e a descrição automaticamente!", with_spaces=True)
###############

# 5. Exemplo de interação com menus: Abre o menu "Arquivo"
# (Substitua pelos nomes dos menus/botões do seu programa)
janela.menu_select("Arquivo -> Salvar como")

print("Automação concluída no Bloco de Notas!")