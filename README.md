# api-cáncer — Entrega técnica reproducible en Machine Learning

Este repositorio contiene una entrega modular reproducible de un flujo de Machine Learning, centrado en la predicción de cáncer a partir de datos estructurados. Incluye entrenamiento, empaquetado, ejecución automatizada, validación CI/CD y contenerización con Docker.

## 🧠 Descripción del proyecto

Se desarrolla una API funcional que permite cargar un modelo previamente entrenado y realizar predicciones sobre nuevos datos. El flujo completo está diseñado para ser reproducible y validado automáticamente.

## 📊 Dataset utilizado

El archivo `datos.csv` contiene registros clínicos anonimizados con variables predictoras y una variable objetivo binaria que indica presencia o ausencia de cáncer. Se realiza preprocesamiento básico, codificación de variables y partición en conjuntos de entrenamiento y prueba.

## 🧪 Modelo aplicado

Se utiliza un modelo de clasificación binaria (`RandomForestClassifier` de `scikit-learn`) entrenado con parámetros estándar. El modelo se evalúa con métricas como:

- Accuracy
- Matriz de confusión
- Reporte de clasificación

El modelo entrenado se guarda como `modelo.pkl` y se expone mediante una API que permite realizar predicciones sobre nuevos datos.

## 🛠️ Estructura del repositorio

- `principal.py`: script principal que carga el modelo y ejecuta la API
- `modelo_de_script_de_entrenamiento.py`: script que entrena y serializa el modelo
- `datos.csv`: conjunto de datos de entrada
- `modelo.pkl`: modelo entrenado y guardado
- `Dockerfile` y `.dockerignore`: configuración del contenedor
- `.github/workflows/`: definición de flujos CI/CD para validación automática
- `solicitud_gcp.json`: ejemplo de configuración para despliegue en GCP
- `requisitos.txt`: dependencias del entorno
- `pruebas/`: carpeta para pruebas funcionales

## 🚀 Ejecución local

```bash
docker build -t api-cancer .
docker run -p 5000:5000 api-cancer

