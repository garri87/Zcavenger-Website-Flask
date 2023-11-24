FROM alpine:3.17

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY . /app


RUN pip install --upgrade pip

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install mysqlclient  

RUN pip install -r requirements.txt

RUN apk del build-deps


#CMD ["python3", "src/index.py"]