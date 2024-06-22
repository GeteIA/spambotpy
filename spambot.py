# Criado por GeteIA 2024 -
import pyautogui
import time

# Espera 8 segundos antes de começar (ajuste conforme necessário)
time.sleep(8)

# Abre o arquivo de texto para leitura com codificação UTF-8
with open("lista.txt", encoding="utf-8") as arquivo:
    # Itera sobre cada linha do arquivo
    for linha in arquivo:

        # Digita a frase da linha atual
        pyautogui.typewrite(linha.strip())  # strip() para remover espaços em branco extras
        # Pressiona Enter
        pyautogui.press("enter")