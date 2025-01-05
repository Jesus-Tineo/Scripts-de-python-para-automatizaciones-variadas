# 🗂️ Suite de Procesamiento de Documentos

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Word](https://img.shields.io/badge/Microsoft_Word-2016+-red.svg)
![Status](https://img.shields.io/badge/Status-Activo-success.svg)

## 📑 Descripción General

Suite profesional para el procesamiento automatizado de documentos Word, que incluye dos herramientas potentes:

1. 🖼️ **Organizador de Imágenes en Word**
   - Reorganiza imágenes en documentos Word
   - Optimiza el diseño y espaciado
   - Procesa múltiples documentos en lote

2. 📄 **Convertidor DOC/DOCX a PDF**
   - Convierte documentos Word a PDF
   - Mantiene el formato original
   - Procesamiento por lotes automático

## ⚙️ Requisitos

```python
# Para el Organizador de Imágenes
python-docx==0.8.11
docx2txt==0.8

# Para el Convertidor PDF
pywin32==305
```

## 🚀 Instalación

```bash
pip install python-docx docx2txt pywin32
```

## 💻 Uso

### 🖼️ Organizador de Imágenes

```python
# Procesar un solo documento
reorganizar_imagenes_en_documento("documento.docx", "ruta_salida")

# Procesar todos los documentos en el directorio
procesar_todos_los_documentos()
```

### 📄 Convertidor a PDF

```python
# Convertir un solo archivo
doc_to_pdf("documento.docx", "salida.pdf")

# Convertir todos los archivos en una carpeta
convert_docs_in_folder("carpeta_entrada", "carpeta_salida")
```

## 🛠️ Características Detalladas

### Organizador de Imágenes

- ✨ **Disposición Optimizada**
  - 2 imágenes por página
  - Centrado automático
  - Espaciado uniforme

- 📏 **Configuración de Página**
  - Tamaño: Letter (8.5" x 11")
  - Márgenes: 0.5" en todos los lados
  - Ancho de imagen: 6 pulgadas

- 🗄️ **Gestión de Archivos**
  - Carpeta temporal para procesamiento
  - Limpieza automática
  - Nombrado inteligente de archivos

### Convertidor PDF

- 🔄 **Conversión Profesional**
  - Mantiene formato original
  - Alta calidad de salida
  - Proceso silencioso (sin interfaz visible)

- 📁 **Gestión de Carpetas**
  - Creación automática de directorios
  - Preservación de nombres de archivo
  - Manejo de errores robusto

## 📋 Ejemplos de Uso

### Organizador de Imágenes
```python
# Configuración personalizada
documento = Document()
section = documento.sections[0]
section.page_width = Inches(8.5)
section.page_height = Inches(11)
```

### Convertidor PDF
```python
# Ejemplo con rutas específicas
input_folder = r'C:\Documentos\Entrada'
output_folder = r'C:\Documentos\PDFs'
convert_docs_in_folder(input_folder, output_folder)
```

## ⚠️ Consideraciones Importantes

1. **Organizador de Imágenes**
   - Requiere permisos de escritura
   - Procesa PNG, JPG y JPEG
   - Memoria suficiente para documentos grandes

2. **Convertidor PDF**
   - Requiere Microsoft Word instalado
   - Windows OS necesario (usa win32com)
   - Cerrar Word antes de usar

## 🔧 Solución de Problemas

### Errores Comunes

1. **Organizador de Imágenes**
   - "Archivo no encontrado": Verificar permisos y rutas
   - "Memoria insuficiente": Reducir tamaño de imágenes

2. **Convertidor PDF**
   - "COM Error": Reinstalar/reparar Microsoft Word
   - "Acceso denegado": Cerrar Word y reintentar

## 🤝 Contribuciones

Áreas de mejora bienvenidas:
- Soporte para más formatos de imagen
- Interfaz gráfica
- Optimización de memoria
- Más opciones de configuración

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.

## 🌟 Apoyo

Si encuentras útil esta suite, ¡considera dar una estrella al repositorio! ⭐
