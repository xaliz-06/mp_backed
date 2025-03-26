# MAJOR PROJECT BACKEND

## Installation

This is a Poetry project in Python so make sure you have Python installed.

- Step 1: Install Poetry

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

- Step 2: Verify installation

```bash
poetry --version
```

- Step 3: Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

- Step 4: Install Dependencies

```bash
poetry install
```

- Step 4: Run the API locally

```bash
poetry run uvicorn src.api.main:app --reload
```

- API Docs
  - Swagger UI: http://127.0.0.1:8000/docs
  - ReDoc: http://127.0.0.1:8000/redoc

## TESTING

Run tests with:

```bash
poetry run pytest
```
