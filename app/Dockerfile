FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14-2021-10-02

ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk --no-cache add --virtual build-dependencies build-base libffi-dev \
    && pip install --no-cache-dir --upgrade -r /app/requirements.txt \
    && apk del build-dependencies

WORKDIR /app

COPY . /app

COPY entrypoint.sh /app

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
