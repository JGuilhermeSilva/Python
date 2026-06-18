'''from pywinauto import Application
import time

# 1. Abre o Bloco de Notas do Windows 11
app = Application(backend="uia").start("notepad.exe")

# 2. Conecta à janela principal (usando o título em português)
janela = app.window(title_re=".*Bloco de Notas.*")
janela.wait("visible", timeout=2)

# --- CORREÇÃO PARA O WINDOWS 11 ---
# No Windows 11, o texto fica dentro de uma área de edição herdada. 
# Usamos 'Edit' para encontrar o campo de texto atualizado.
campo_texto = janela.child_window(control_type="Edit")

# 3. Digita o texto (o parâmetro 'click_input' força um clique antes de digitar)
campo_texto.click_input()
campo_texto.type_keys("Testando a automacao no Windows 11!", with_spaces=True)

print("Funcionou!")'''
import time
import subprocess
from pywinauto import Application

# 1. Abre o programa pelo próprio sistema operacional (independente do processo)
# Substitua pelo comando ou caminho correto do seu aplicativo
#subprocess.Popen("notepad.exe") 
subprocess.Popen("Taskmgr.exe")
# 2. Aguarda alguns segundos para garantir que a interface gráfica abriu
time.sleep(3)

try:
    # 3. Conecta à janela usando um título parcial (procura por qualquer janela que CONTENHA esse texto)
    # IMPORTANTE: Altere "Bloco de Notas" para uma palavra que apareça no título do SEU programa!
    app = Application(backend="uia").connect(title_re=".*Gerenciador de Tarefas*", timeout=5)
    
    # 4. Captura a janela conectada
    janela = app.top_window()
    
    # 5. Salva os identificadores no arquivo de texto
    janela.print_control_identifiers(filename="meus_controles_GerenciadorTarefas.txt")
    print("✅ Sucesso! Os identificadores foram salvos no arquivo 'meus_controles_GerenciadorTarefas.txt'.")

except Exception as e:
    print(f"❌ Erro ao conectar: {e}")