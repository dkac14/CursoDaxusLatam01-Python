import yfinance
import matplotlib
import pyautogui
import pyperclip
import webbrowser
import time

# Obtiene datos bursátiles usando el código de la empresa (Apple)
# history("6mo") descarga datos de los últimos 6 meses
data = yfinance.Ticker("AAPL").history("6mo")

# Extrae los valores de cierre de las acciones
close = data.Close

# Grafica el comportamiento del precio de cierre
close.plot()

# Calcula el valor máximo, mínimo y promedio del cierre
# Los resultados se redondean a dos decimales
maximo = round(close.max(), 2)
minimo = round(close.min(), 2)
promedio = round(close.mean(), 2)

# Abre Gmail en el navegador
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

# Define los datos del correo
to = "domenicaamores2006@gmail.com"
subject = "Correo de Prueba"

# Crea el cuerpo del correo con los resultados obtenidos
body = f"""
Buenas tardes, esto es un correo de prueba para la practica
del proyecto02 de DaxusLatam de automatizacion.

max = {maximo}
min = {minimo}
mean = {promedio}
"""

# Espera unos segundos para que cargue Gmail
time.sleep(3)

# Define una pausa automática entre acciones del mouse y teclado
pyautogui.PAUSE = 3

# Hace clic en el botón "Redactar"
pyautogui.click(172, 304)

# Pega el correo del destinatario
pyperclip.copy(to)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Pega el asunto del correo
pyperclip.copy(subject)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Pega el cuerpo del mensaje
pyperclip.copy(body)
pyautogui.hotkey("ctrl", "v")

# Hace clic en el botón "Enviar"
pyautogui.click(1630, 1485)
