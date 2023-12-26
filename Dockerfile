FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN python -m venv env

RUN source env/bin/activate

RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev build-base postgresql-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del build-base

COPY . .

CMD ["python3", "src/index.py"]
