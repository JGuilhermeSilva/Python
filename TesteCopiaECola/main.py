'''import pyperclip as pc

texto2 = pc.paste()
print(texto2)'''

import pyautogui
import pyperclip
import time

print("Mova o mouse para a posição desejada. Pressione Ctrl+C no terminal para parar.")

try:
    while True:
        # Pega as coordenadas X e Y do mouse em tempo real
        x, y = pyautogui.position()
        # Formata a saída para exibir as coordenadas no console
        posicao = f'Coordenadas atuais: X = {x}, Y = {y}'
        print(posicao, end='\r')
        
        # Pausa de 0.1 segundos para não sobrecarregar o processador
        time.sleep(0.1)
        #ao colocar o mouse em cma do x de fechar a aba clica
        if x>=1320 and x<=1365 and y>=2 and y<=372:
            pyautogui.click(x=1335,y=28, clicks=1)
            #1324,1365
        if x>=432 and x<=500 and y>=517 and y<=547:
            pyautogui.click(x=673, y=394, clicks=1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            texto_copiado = pyperclip.paste()
            pyautogui.hotkey('win', 'r')
            pyautogui.write('notepad')
            pyautogui.hotkey('enter')
            time.sleep(1)
            #pyautogui.write(texto_copiado)
            pyautogui.hotkey('ctrl', 'v')

        
#O KeyboardInterrupt força a parada de um programa pressionando Ctrl + C        
except KeyboardInterrupt:
    print(texto_copiado)
    print('\nPrograma encerrado.')
    ############################
    #teste encerrado
    ######################