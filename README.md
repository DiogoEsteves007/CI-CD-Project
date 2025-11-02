Teste

Objetivo:

    Criar um pipeline automatizado de Machine Learning que:

    Treina um modelo ML simples (ex: previsão de churn).

    Testa e valida o código automaticamente via GitHub Actions.

    Cria e faz push de uma imagem Docker.

    Faz deploy automático de uma API (FastAPI) para servir o modelo.


Activate venv:  .\mlopsVenv\Scripts\Activate.ps1
Libraries:  pip install scikit-learn fastapi uvicorn pytest joblib




MLOps/
├── data/
│   └── raw.csv
├── src/
│   ├
│   ├── train.py
│   ├
│   └── model.joblib
├── app/
│   └── main.py
├── tests/
│   └── test_train.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
