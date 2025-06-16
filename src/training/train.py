"""Train a simple forecasting model."""
from pathlib import Path

MLFLOW_TRACKING_URI = Path(__file__).resolve().parents[2] / "mlruns"
MODEL_PATH = Path(__file__).resolve().parents[2] / "model.joblib"


def main() -> None:
    import joblib
    import mlflow
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error

    from .data import load_data

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI.as_uri())
    mlflow.sklearn.autolog()

    df = load_data()
    X = df[["store", "sku"]]
    y = df["sales"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"MAE: {mae:.2f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
