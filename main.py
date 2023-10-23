import pyautogui #bblioteca para identificaçãod e eventos no computador baixe com pip install pyautogui
import keyboard #biblioteca para identificar eventos no teclado baixe com pip install keyboard
altura = 4
largura = 300
captura =(213, 865, largura, altura)
ecra = pyautogui.screenshot(region=captura)
ecra.save('ecra.png')

def identifica_vermelho(imagem):
    altura_imagem , largura_imagem = imagem.size
    for x in range(0, altura_imagem):
        for y in range(0, largura_imagem):
            if imagem.getpixel((x, y)) == (255, 0, 0):
                return x, y

def identifica_preto(imagem):
    while imagem.getpixel((1, 1)) != (255,255,255):
       imagem = pyautogui.screenshot(region =(213 , distancia,2,2))
       pyautogui.mouseDown()
    pyautogui.mouseUp()       

while not keyboard.is_pressed('m'):
    pixel_vermelho = identifica_vermelho(ecra)
    if pixel_vermelho:
        distancia = pixel_vermelho[0]
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])
        pixel_preto = pyautogui.screenshot(region =(213 , distancia,2,2))
        identifica_preto(pixel_preto)
        #pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])
        
        
        identifica_preto(ecra, distancia)
    pyautogui.sleep(0.016)
    pyautogui.mouseUp()
    ecra = pyautogui.screenshot(region=captura)

    
#pyautogui.moveTo(largura,altura, duration=0.1)