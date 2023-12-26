FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev build-base && \
    python -m venv env && \
    source env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del build-base

COPY . .

CMD ["python3", "src/index.py"]
