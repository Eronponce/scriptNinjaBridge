import pyautogui #bblioteca para identificaçãod e eventos no computador baixe com pip install pyautogui
import keyboard #biblioteca para identificar eventos no teclado baixe com pip install keyboard
altura = 600
largura = 500
captura =(360, 320, altura, largura)
ecra = pyautogui.screenshot(region=captura)

def identifica_vermelho(imagem):
    altura_imagem , largura_imagem = imagem.size
    for x in range(0, altura_imagem):
        for y in range(0, largura_imagem):
            if imagem.getpixel((x, y)) == (255, 0, 0):
                return x, y
    
while not keyboard.is_pressed('m'):
    pixel_vermelho = identifica_vermelho(ecra)
    if pixel_vermelho:
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])
        pyautogui.mouseDown()
    pyautogui.sleep(0.016)
    ecra = pyautogui.screenshot(region=captura)
#pyautogui.moveTo(largura,altura, duration=0.1)