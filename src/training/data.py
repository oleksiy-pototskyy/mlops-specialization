from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_FILE = DATA_DIR / "sales.csv"


def generate_sample_data(rows: int = 1000):
    import pandas as pd
    rng = pd.date_range("2021-01-01", periods=rows, freq="D")
    df = pd.DataFrame({
        "date": rng,
        "store": (rng.day % 10),
        "sku": (rng.dayofyear % 50),
        "sales": (rng.day * rng.dayofyear) % 100,
    })
    return df


def load_data():
    import pandas as pd
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE)
    else:
        df = generate_sample_data()
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(DATA_FILE, index=False)
    return df
