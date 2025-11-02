Mini Project — CI/CD + Docker + API

Este é um mini projeto focado em demonstrar conhecimentos práticos de **MLOps**, **CI/CD**, **testes automáticos** e **Docker** utilizando GitHub Actions.  
O objetivo principal é mostrar a capacidade de automatizar um pipeline simples desde o treino de um modelo até à disponibilização de uma API para predições.

---

## 🚀 Funcionalidades

✅ Treino automático de um modelo de Machine Learning  
✅ API com endpoint de predição (`/predict`)  
✅ Pipeline CI/CD com GitHub Actions  
✅ Testes automáticos com `pytest`  
✅ Build automatizado de imagem Docker  
✅ Deploy automático da imagem para o Docker Hub  
✅ Execução containerizada com `docker run`  
✅ Reprodutibilidade total

---

## Estrutura do projeto

MLOps/
├── data/
│ └── raw.csv
├── src/
│ ├── train.py
│ └── model.joblib
├── app/
│ └── main.py
├── tests/
│ └── test_train.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
├── .github/
│ └── workflows/
│ └── ci-cd.yml
└── README.md

---

## Tecnologias utilizadas

- Python 3.10
- FastAPI (ou Flask, caso tenhas usado)
- Scikit-Learn
- Joblib
- Docker
- GitHub Actions
- PyTest

---

```bash
pytest


