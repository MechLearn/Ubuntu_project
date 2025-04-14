# tests/test_model.py
def test_model_output():
    from joblib import load
    import numpy as np

    model = load("models/modelo.pkl")
    pred = model.predict(np.array([[5.1, 3.5, 1.4, 0.2]]))
    assert pred[0] in [0, 1, 2]
