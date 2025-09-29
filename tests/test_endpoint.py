import requests

try:
    response = requests.get("http://localhost:8080/health")
    print("Status code:", response.status_code)
    print("Response body:", response.text)
    assert response.status_code == 200
except Exception as e:
    print("Error al conectar con el endpoint:", e)
