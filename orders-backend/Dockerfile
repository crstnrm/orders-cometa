FROM python:3.11-buster AS builder

RUN pip install --upgrade pip && pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /cometa

COPY pyproject.toml poetry.lock* ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root

FROM python:3.11-slim-buster AS runtime

ENV VIRTUAL_ENV=/cometa/.venv \
    # Keeps Python from generating .pyc files in the container
    PYTHONUNBUFFERED=1 \  
    # Turns off buffering for easier container logging
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/cometa/.venv/bin:${PATH}"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /cometa/code

CMD ["uvicorn", "web.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


