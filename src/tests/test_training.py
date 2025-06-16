import sys
from pathlib import Path
import importlib
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.training import data, train


@pytest.mark.skipif(importlib.util.find_spec('pandas') is None, reason='pandas missing')
def test_generate_data() -> None:
    df = data.generate_sample_data(rows=10)
    assert not df.empty


@pytest.mark.skipif(importlib.util.find_spec('sklearn') is None, reason='sklearn missing')
def test_train(tmp_path) -> None:
    orig_model_path = train.MODEL_PATH
    train.MODEL_PATH = tmp_path / "model.joblib"
    train.main()
    assert train.MODEL_PATH.exists()
    train.MODEL_PATH = orig_model_path
