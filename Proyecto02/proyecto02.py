import yfinance
import matplotlib

#Con yfinance, a traves de Ticker colocmaos el codigo de la empresa y history permite de que rango
#de fecha poner los datos
data = yfinance.Ticker("AAPL").history("6mo")

#Accedemos a High de data
close = data.Close

#Realizar una grafica de los datos obtenidos
close.plot()





