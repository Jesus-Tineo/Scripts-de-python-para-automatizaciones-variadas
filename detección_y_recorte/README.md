# 🎯 Detector Inteligente de Personas con Auto-Recorte

![Versión Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Licencia](https://img.shields.io/badge/licencia-MIT-red.svg)

## 🚀 Descripción General

¡Esta potente herramienta de visión por computadora detecta automáticamente personas en imágenes y las recorta de manera inteligente con márgenes personalizables! Es perfecta para procesar grandes conjuntos de imágenes donde necesitas enfocarte en sujetos humanos.

## ✨ Características Principales

- 🔍 Detección avanzada de personas usando el modelo MobileNet SSD
- ⚡ Capacidad de procesamiento por lotes de múltiples imágenes
- 🎯 Recorte inteligente con márgenes personalizables
- 📁 Gestión automática del directorio de salida
- 🎚️ Umbral de confianza ajustable
- 🖼️ Preserva la calidad de la imagen

## 🛠️ Requisitos

- Python 3.6+
- OpenCV (cv2)
- Archivos del modelo SSD MobileNet:
  - `SSD_MobileNet_prototxt.txt`
  - `SSD_MobileNet.caffemodel`

## 📦 Instalación

```bash
# Clona este repositorio
git clone https://github.com/Jesus-Tineo/Scripts-de-python-para-automatizaciones-variadas/tree/main/detecci%C3%B3n_y_recorte

# Instala los paquetes requeridos
pip install opencv-python
```

## 🔧 Configuración

Antes de ejecutar el script, configura estos parámetros clave:

```python
carpeta = 'ruta/a/tus/imagenes'  # Directorio de imágenes de entrada
carpeta_salida = 'recortes_con_margen'  # Directorio de salida
margen = 500  # Tamaño del margen en píxeles
```

## 🚀 Uso

1. Coloca tus imágenes en el directorio de entrada
2. Ejecuta el script:
```bash
python detector_personas.py
```
3. Encuentra tus imágenes recortadas en el directorio de salida

## 💡 Cómo Funciona

1. **Carga de Imágenes**: Procesa cada imagen del directorio de entrada
2. **Detección de Personas**: Utiliza MobileNet SSD para identificar personas con alta precisión
3. **Recorte Inteligente**: Determina automáticamente los límites óptimos de recorte
4. **Adición de Márgenes**: Agrega márgenes especificados manteniéndose dentro de los límites de la imagen
5. **Generación de Salida**: Guarda las imágenes procesadas con la calidad original

## ⚙️ Configuración Avanzada

- Ajusta el umbral de confianza (predeterminado: 0.5)
- Modifica la clase de detección (clase persona = 15)
- Cambia los parámetros de preprocesamiento de imágenes

## 📝 Notas

- Las imágenes se procesan manteniendo su resolución original
- Soporta formatos comunes de imagen (PNG, JPG, JPEG)
- Omite automáticamente las imágenes sin detecciones de personas

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:
- Reportar errores
- Proponer nuevas funciones
- Crear pull requests

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 🌟 ¡Danos una Estrella!

Si encuentras útil esta herramienta, ¡por favor dale una estrella a nuestro repositorio! ⭐
