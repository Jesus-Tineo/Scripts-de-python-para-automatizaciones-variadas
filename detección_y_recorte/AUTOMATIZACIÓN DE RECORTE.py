import cv2
import os

# Definir la carpeta donde están las imágenes
carpeta = 'ruta_del_archivo'

# Definir el modelo de detección de personas
modelo = cv2.dnn.readNetFromCaffe("SSD_MobileNet_prototxt.txt", "SSD_MobileNet.caffemodel")

# Crear la carpeta de salida si no existe
carpeta_salida = 'recortes_con_margen'
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Tamaño del margen
margen = 500

# Recorrer las imágenes de la carpeta
for archivo in os.listdir(carpeta):
    # Leer la imagen
    imagen = cv2.imread(os.path.join(carpeta, archivo))
    # Obtener las dimensiones de la imagen
    alto, ancho = imagen.shape[:2]
    # Preprocesar la imagen para el modelo
    blob = cv2.dnn.blobFromImage(imagen, 0.007843, (300, 300), 127.5)
    # Pasar la imagen por el modelo
    modelo.setInput(blob)
    # Obtener las detecciones del modelo
    detecciones = modelo.forward()
    
    # Inicializar las coordenadas del cuadro delimitador que contiene a todas las personas
    x_min, y_min, x_max, y_max = ancho, alto, 0, 0

    # Recorrer las detecciones
    for i in range(detecciones.shape[2]):
        # Obtener la confianza de la detección
        confianza = detecciones[0, 0, i, 2]
        # Si la confianza es mayor que un umbral
        if confianza > 0.5:
            # Obtener la clase de la detección
            clase = int(detecciones[0, 0, i, 1])
            # Si la clase es 15, corresponde a una persona
            if clase == 15:
                # Obtener las coordenadas del cuadro delimitador de la persona
                x1 = int(detecciones[0, 0, i, 3] * ancho)
                y1 = int(detecciones[0, 0, i, 4] * alto)
                x2 = int(detecciones[0, 0, i, 5] * ancho)
                y2 = int(detecciones[0, 0, i, 6] * alto)

                # Actualizar las coordenadas del cuadro delimitador que contiene a todas las personas
                x_min = min(x_min, x1 - margen)
                y_min = min(y_min, y1 - margen)
                x_max = max(x_max, x2 + margen)
                y_max = max(y_max, y2 + margen)

    # Verificar si se detectaron personas y actualizar la imagen
    if x_min < x_max and y_min < y_max:
        recorte = imagen[max(0, y_min):min(alto, y_max), max(0, x_min):min(ancho, x_max)]
        # Guardar el recorte en la carpeta de salida
        cv2.imwrite(os.path.join(carpeta_salida, archivo), recorte)

print("Proceso completado.")

