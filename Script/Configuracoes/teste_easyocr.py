import pyautogui as PY
import easyocr
import numpy as np

# ==========================================
# 1. O CÉREBRO DA IA (Instanciado UMA única vez)
# ==========================================
print("[INFO] Carregando os 'pesos' da Inteligência Artificial na RAM...")
print("[INFO] Isso pode demorar alguns segundos na primeira execução.")

# gpu=False garante que ele rode no seu Processador (CPU) sem dar erro caso seu PC não tenha o CUDA da NVIDIA configurado.
leitor_ia = easyocr.Reader(['en'], gpu=False) 

# ==========================================

def testar_leitura_poder():
    print("\nPosicione a tela do Hero Wars nos adversários da Grande Arena.")
    print("Você tem 5 segundos...")
    PY.sleep(5)
    
    # 2. O Recorte
    # (Você terá que calibrar esse X, Y, Largura, Altura usando o seu capturador de coordenadas depois)
    regiao_poder = (500, 300, 150, 50) 
    print(f"\nCapturando região: {regiao_poder}")
    
    imagem_bruta = PY.screenshot(region=regiao_poder)
    
    # O EasyOCR não lê a imagem do PyAutoGUI direto, precisamos converter para Numpy Array
    imagem_array = np.array(imagem_bruta)

    # 3. A Leitura Filtrada
    # allowlist='0123456789' é a nossa trava de segurança. Força a IA a ignorar letras e ler APENAS números.
    print("[INFO] Lendo a imagem...")
    resultados = leitor_ia.readtext(imagem_array, allowlist='0123456789')
    
    print("\n" + "="*40)
    if resultados:
        # O EasyOCR devolve uma lista. Cada item tem: [coordenadas_da_caixa, texto_lido, nivel_de_confianca]
        texto_lido = resultados[0][1]
        confianca = resultados[0][2]
        print(f"RESULTADO DO OCR: '{texto_lido}'")
        print(f"Nível de Confiança da IA: {confianca:.2%}")
    else:
        print("A IA não encontrou nenhum número nessa região da tela.")
    print("="*40)

if __name__ == "__main__":
    testar_leitura_poder()