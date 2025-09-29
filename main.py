"""
main.py

API REST construida con Flask para servir un modelo de clasificación binaria
entrenado con el dataset Breast Cancer Wisconsin y RandomForest.
Incluye endpoints para predicción, verificación de estado, configuración dinámica,
eliminación del modelo y mensaje de bienvenida.
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo entrenado
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
    if not data or "features" not in data or len(data["features"]) != 30:
        return jsonify({"error": "Datos mal estructurados o incompletos"}), 400

    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = modelo.predict(features)[0]
        probas = modelo.predict_proba(features)[0].tolist()
        return jsonify({
            "prediction": int(prediction),
            "probabilities": probas
        }), 200
    except Exception as e:
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
    # Ejecuta la API en el puerto 8000, compatible con Dockerfile
    app.run(host="0.0.0.0", port=8000)
