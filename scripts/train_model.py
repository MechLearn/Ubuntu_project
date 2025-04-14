
# scripts/train_model.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Cargar datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# 2. Entrenar modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 3. Crear carpeta models si no existe
os.makedirs("models", exist_ok=True)

# 4. Guardar modelo como .pkl
joblib.dump(model, "models/modelo.pkl")
print("✅ Modelo guardado en models/modelo.pkl")


