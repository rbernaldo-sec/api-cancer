# 1. Imagen base oficial de Python optimizada para producción
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos del proyecto al contenedor
# Archivo con dependencias del proyecto
COPY requirements.txt .

# Script principal que levanta la API Flask
COPY main.py .

# Modelo entrenado serializado con joblib
COPY model.pkl .

# 4. Instalar las dependencias necesarias sin guardar caché
RUN pip install --no-cache-dir -r requirements.txt

# 5. Exponer el puerto 5000 para acceso externo a la API
EXPOSE 5000

# 6. Comando que ejecuta la API al iniciar el contenedor
CMD ["python", "main.py"]

