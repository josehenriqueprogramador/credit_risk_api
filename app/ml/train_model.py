import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import os

OUT = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(OUT, exist_ok=True)
MODEL_PATH = os.path.join(OUT, "model.joblib")

def gen_data(n=1000, random_state=42):
    rng = np.random.RandomState(random_state)
    idade = rng.randint(18, 75, size=n)
    renda = rng.normal(3000, 1500, size=n).clip(500)
    historico = rng.randint(0, 10, size=n)
    # target: higher renda and lower historico => lower default
    score = (renda / 10000) - (historico / 20) + (idade / 100)
    prob = 1 / (1 + np.exp(- (score - 0.2)))
    y = (prob > 0.5).astype(int)
    df = pd.DataFrame({
        "idade": idade,
        "renda_mensal": renda,
        "historico_credito": historico,
        "inadimplente": y
    })
    return df

def train_and_save():
    df = gen_data(2000)
    X = df[["idade", "renda_mensal", "historico_credito"]]
    y = df["inadimplente"]
    model = RandomForestClassifier(n_estimators=50, random_state=0)
    model.fit(X.values, y.values)
    dump(model, MODEL_PATH)
    print("Model treinado e salvo em:", MODEL_PATH)

if __name__ == "__main__":
    train_and_save()
