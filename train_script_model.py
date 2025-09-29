"""
train_script_cancer.py

Este script entrena un modelo de clasificación binaria utilizando el dataset Breast Cancer Wisconsin
y el algoritmo RandomForest. El modelo se guarda como 'model.pkl' para ser utilizado
posteriormente en una API Flask.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# 1. Cargar dataset Breast Cancer
df = pd.read_csv("data.csv")

# 2. Limpieza de columnas irrelevantes
# Eliminar 'id' y 'Unnamed: 32' si existen
columnas_a_eliminar = [col for col in ["id", "Unnamed: 32"] if col in df.columns]
df.drop(columns=columnas_a_eliminar, axis=1, inplace=True)

# 3. Codificar diagnóstico binario
df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

# 4. Separación de variables
X = df.drop("diagnosis", axis=1)
y = df["diagnosis"]

print(f"✅ Columnas usadas para entrenamiento: {X.shape[1]}")  # Debe imprimir 30

# 5. División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Entrenamiento
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 7. Evaluación
y_pred = modelo.predict(X_test)
print("✅ Reporte de clasificación:")
print(classification_report(y_test, y_pred))

# 8. Guardar modelo
joblib.dump(modelo, "model.pkl")
print("✅ Modelo guardado como model.pkl")
