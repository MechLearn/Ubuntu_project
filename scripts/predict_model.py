# scripts/predict_model.py

import joblib
import numpy as np

# 1. Cargar modelo
model = joblib.load("models/modelo.pkl")

# 2. Crear una muestra para predecir
sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Ejemplo tipo Iris

# 3. Predecir
prediccion = model.predict(sample)
print(f"🌼 Clase predicha: {prediccion[0]}")
