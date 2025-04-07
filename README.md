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
git clone https://github.com/xaliz-06/mp_backed.git
cd mp_backed
```

- Step 4: Install Dependencies

```bash
poetry install
```

- Step 4: Run the API locally

```bash
poetry run uvicorn src.major_project.api.main:app --reload
```

- Step 5: Install and run `ngrok` to create a static public URL that tunnels to your local backend (must be configured with my `ngrok` token)

```bash
ngrok http --url=marginally-huge-skylark.ngrok-free.app 8000
```

- API Docs
  - Swagger UI: http://127.0.0.1:8000/docs
  - ReDoc: http://127.0.0.1:8000/redoc

## TESTING

Run tests with:

```bash
poetry run pytest
```
