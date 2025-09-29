# 1. Imagen base oficial de Python
FROM python:3.10-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar archivos del proyecto
COPY requirements.txt .
COPY main.py .
COPY model.pkl .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Exponer puerto Flask
EXPOSE 8000

# 6. Comando de ejecución
CMD ["python", "main.py"]
