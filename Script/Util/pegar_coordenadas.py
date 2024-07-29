import pyautogui

print("Posicione o mouse no local desejado e pressione Enter.")
input("Pressione Enter para capturar as coordenadas...")

# Captura as coordenadas atuais do mouse
x, y = pyautogui.position()
print(f"As coordenadas do mouse são: X={x}, Y={y}")
