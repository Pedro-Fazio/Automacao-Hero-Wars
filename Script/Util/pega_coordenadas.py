import pyautogui
print('\nAperte Ctrl-C para sair.')
try:
    while True:
        x, y = pyautogui.position()
        posicao = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(posicao, end='')
        print('\b' * len(posicao), end='', flush=True)
except KeyboardInterrupt:
    print('\n')