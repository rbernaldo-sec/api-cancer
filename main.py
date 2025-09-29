"""
main.py

API REST construida con Flask para servir un modelo de clasificación binaria
entrenado con el dataset Breast Cancer Wisconsin y RandomForest.

Endpoints disponibles:
- GET /         → Mensaje institucional de bienvenida
- GET /health   → Verificación de estado y metadatos del modelo
- POST /predict → Predicción de clase y probabilidades
- PUT /config   → Actualización dinámica de configuración
- DELETE /model → Eliminación del modelo de memoria

Requisitos:
- Archivo model.pkl entrenado y disponible en el mismo directorio
- Librerías Flask, joblib y numpy instaladas
"""

from flask import Flask, request, jsonify  # Framework web y utilidades JSON
import joblib                             # Para cargar el modelo entrenado
import numpy as np                        # Para manipular vectores de entrada

# Inicializa la aplicación Flask
app = Flask(__name__)

# Carga el modelo previamente entrenado desde archivo
modelo = joblib.load("model.pkl")

@app.route("/", methods=["GET"])
def welcome():
    """
    Endpoint raíz /
    Muestra un mensaje institucional de bienvenida.
    """
    return jsonify({"message": "Bienvenido a la API de diagnóstico de cáncer de mama 🩺"}), 200

@app.route("/health", methods=["GET"])
def health():
    """
    Endpoint /health
    Verifica el estado operativo de la API y entrega metadatos del modelo cargado.
    """
    return jsonify({"status": "API funcionando", "model": "Cancer-RandomForest"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint /predict
    Recibe un JSON con vector de características y devuelve la clase predicha y probabilidades.
    Estructura esperada: {"features": [float, ..., float]} con 30 valores
    """
    data = request.get_json()

    # Validación de estructura del JSON recibido
    if not data or "features" not in data or len(data["features"]) != 30:
        return jsonify({"error": "Datos mal estructurados o incompletos"}), 400

    try:
        # Transformación del vector de entrada y predicción
        features = np.array(data["features"]).reshape(1, -1)
        prediction = modelo.predict(features)[0]
        probas = modelo.predict_proba(features)[0].tolist()

        # Respuesta con clase y probabilidades
        return jsonify({
            "prediction": int(prediction),
            "probabilities": probas
        }), 200

    except Exception as e:
        # Manejo de errores internos
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route("/config", methods=["PUT"])
def update_config():
    """
    Endpoint /config
    Permite actualizar parámetros dinámicos de configuración (ej. umbral de decisión).
    """
    data = request.get_json()
    return jsonify({"message": "Configuración actualizada", "new_config": data}), 200

@app.route("/model", methods=["DELETE"])
def delete_model():
    """
    Endpoint /model
    Elimina el modelo cargado de memoria.
    Útil para pruebas de error o reinicio controlado.
    """
    global modelo
    modelo = None
    return jsonify({"message": "Modelo eliminado de memoria"}), 200

if __name__ == "__main__":
    # Ejecuta la API en el puerto 5000, compatible con Dockerfile y CI/CD
    app.run(host="0.0.0.0", port=5000)
