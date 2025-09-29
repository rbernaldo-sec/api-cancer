"""
Script de prueba para validar el estado del endpoint /health de la API REST.

Este script realiza una solicitud GET a http://localhost:5000/health,
verifica que la respuesta sea exitosa (código 200) y muestra el contenido recibido.

Requisitos:
- La API debe estar corriendo en el puerto 5000
- La librería 'requests' debe estar instalada
"""

import requests  # Librería para realizar solicitudes HTTP

# Intentamos conectar al endpoint /health
try:
    response = requests.get("http://localhost:5000/health")  # Solicitud GET

    # Mostramos el código de estado y el cuerpo de la respuesta
    print("Status code:", response.status_code)
    print("Response body:", response.text)

    # Verificamos que la respuesta sea exitosa
    assert response.status_code == 200  # Validación del estado esperado

except Exception as e:
    # En caso de error de conexión o ejecución
    print("Error al conectar con el endpoint:", e)

