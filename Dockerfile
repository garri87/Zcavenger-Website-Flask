FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add --no-cache build-base postgresql-dev && \
    python -m venv env && \
    env/bin/pip install --upgrade pip && \
    env/bin/pip install -r requirements.txt && \
    apk del build-base

COPY . .

CMD ["python3", "src/index.py"]
