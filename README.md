# Retail MLOps Specialization Project

This repository provides a lightweight but realistic end-to-end MLOps project used across the `MLOps Specialization` course https://nubes.academy It demonstrates data versioning, feature engineering, training, serving and infrastructure automation on Kubernetes.

## Repository layout

```
retail-mlops/
├── data/                # raw data tracked with DVC (placeholder)
├── features/            # Feast feature definitions
├── src/
│   ├── training/        # reusable training package
│   ├── serving/         # FastAPI app for inference
│   └── tests/           # unit tests
├── pipelines/           # Argo Workflows or Kubeflow pipelines
├── infra/
│   ├── terraform/       # per-cloud modules
│   └── k8s/             # Helm charts/Kustomize templates
├── .github/workflows/   # CI configuration
└── dashboards/          # Grafana / QuickSight templates
```

The project trains a simple demand forecasting model from the open M5 Forecasting dataset and exposes predictions through a FastAPI service running on Kubernetes.

## Getting started

1. Install the Python dependencies (see `src/requirements.txt`).
2. Run `python src/training/train.py` to train a baseline model and log it with MLflow.
3. Launch the FastAPI app via `uvicorn src.serving.main:app`.

CI checks can be executed locally via `pre-commit` or by pushing to GitHub which triggers the workflow defined in `.github/workflows/ci.yml`.

