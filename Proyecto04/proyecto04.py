# Importa OpenCV para el uso de la cámara y procesamiento de imágenes
import cv2  
# Importa el detector de manos de cvzone
from cvzone.HandTrackingModule import HandDetector  

webCam = cv2.VideoCapture(0)  # Activa la cámara web del equipo
rastreador = HandDetector(detectionCon=0.8, maxHands=2)  # Configura el detector de manos

while True:  # Bucle infinito para capturar video en tiempo real
    
    exito, imagen = webCam.read()  # Lee un fotograma desde la cámara
    imagen = cv2.resize(imagen, (1200, 720))  # Redimensiona la imagen capturada
    coordenadas, imagen_manos = rastreador.findHands(imagen)  # Detecta las manos en la imagen
    cv2.imshow("Proyecto Web IA", imagen)  # Muestra la imagen en una ventana
    
    if cv2.waitKey(1) != -1:  # Finaliza el programa si se presiona cualquier tecla
        break
    
webCam.release()  # Libera el uso de la cámara web
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas
