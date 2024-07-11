# FastAPI template

Opinionated FastAPI template to quickstart my projects (Usually internal APIs).

It is a fork of [dunossauro/fastapi-do-zero](https://github.com/dunossauro/fastapi-do-zero) class 12 with modifications:

- Using SQLModel
- CLI utility
- The only model is User. Routes to create and read users require authentication. First user must be created through CLI utility.
- Directories for Models and Schemas
- Documentation protected. Requires Authentication

Problaby good way to start this project: Use a Code Editor to replace all 'fastapi_template' and 'fastapi-template' with your project name

## Run locally

```bash
poetry install
```

```bash
alembic upgrade head
```

```bash
poetry run fastapi dev fastapi_template/app.py
```

## Run with Docker

```bash
docker-compose up
```

## Run CLI
```bash
poetry run fastapi_template/cli.py --help
```

## Run tests
```bash
poetry run task test
```


