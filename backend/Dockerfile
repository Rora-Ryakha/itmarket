FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install gunicorn

WORKDIR /app/backend

COPY requirements.txt .

RUN apk add --virtual .build-deps --no-cache  postgresql-dev gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && apk --purge del .build-deps

COPY . .

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/backend/entrypoint.sh"]
