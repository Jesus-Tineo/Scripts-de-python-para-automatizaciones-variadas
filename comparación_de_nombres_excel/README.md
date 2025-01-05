# 🔍 Sistema Inteligente de Comparación de Nombres

![Versión Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.0+-green.svg)
![Licencia](https://img.shields.io/badge/licencia-MIT-red.svg)

## 🎯 Descripción General

Sistema avanzado para comparar nombres entre dos bases de datos Excel, diseñado específicamente para manejar variaciones en la escritura de nombres y apellidos. Ideal para:
- Verificación de registros
- Validación de bases de datos
- Detección de duplicados
- Normalización de nombres

## ✨ Características Principales

- 🧠 Comparación inteligente que tolera variaciones comunes
- 📊 Procesamiento de archivos Excel
- 🔄 Normalización automática de nombres
- ⚡ Alta eficiencia en grandes volúmenes de datos
- 📝 Generación automática de reportes

## 🛠️ Versiones Disponibles

### Versión 1: Comparación Avanzada
- Normalización y ordenamiento de palabras
- Manejo de variaciones ortográficas (v/b, s/c/z, i/y)
- Umbral de similitud configurable
- Nombre de archivo de salida personalizado

### Versión 2: Comparación Simple
- Normalización básica de texto
- Comparación directa con umbral
- Salida estandarizada
- Proceso más ligero

## 📦 Requisitos

```python
import pandas as pd
import re
from difflib import SequenceMatcher
import os
```

## 🚀 Uso

1. Prepara tus archivos Excel:
   - Archivo base con columna "APELLIDOS Y NOMBRES"
   - Archivo a comparar con columna "NOMBRES Y APELLIDOS"

2. Configura las rutas:
```python
base_file_path = 'Archivo1.xlsx'
solicitud_file_path = 'Archivo2.xlsx'
```

3. Ajusta el umbral de similitud según necesites:
```python
similarity_threshold = 0.80  # 80% de similitud requerida
```

4. Ejecuta el script y obtén resultados en formato Excel

## ⚙️ Personalización

### Ajustes de Normalización
```python
# Personaliza las reglas de normalización
name = re.sub(r'[vb]', 'b', name)  # v/b
name = re.sub(r'[scz]', 's', name)  # s/c/z
name = re.sub(r'[iy]', 'i', name)   # i/y
```

### Umbral de Similitud
- Version 1: `similarity_threshold = 0.80`
- Version 2: `threshold = 0.75`

## 📊 Resultados

El sistema genera un nuevo archivo Excel con:
- Todos los registros originales
- Nueva columna "Resultado Comparación" o "Estado"
- Indicador "Encontrado" o "No encontrado"

## 💡 Mejores Prácticas

1. **Preparación de Datos**
   - Verificar formatos de columnas
   - Eliminar filas vacías
   - Estandarizar nombres de columnas

2. **Ajuste de Parámetros**
   - Probar diferentes umbrales
   - Ajustar reglas de normalización
   - Validar resultados

3. **Procesamiento**
   - Usar la versión adecuada según volumen
   - Verificar memoria disponible
   - Hacer respaldo de archivos

## 🤝 Contribuciones

¡Contribuciones bienvenidas! Áreas de mejora:
- Optimización de rendimiento
- Nuevas reglas de normalización
- Interfaces gráficas
- Soporte para más formatos

## ⚠️ Consideraciones

- El tiempo de procesamiento depende del tamaño de los archivos
- Mayor umbral = más precisión pero menos coincidencias
- Menor umbral = más coincidencias pero posibles falsos positivos

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## 🌟 ¡Apoya el Proyecto!

Si este sistema te resulta útil, ¡no olvides darle una estrella al repositorio! ⭐
