FROM python:3.9-alpine
RUN apk add --no-cache gcc \
                       musl-dev \
                       mariadb-connector-c-dev \
    && rm -rf /var/cache/apk/*
ENV PYTHONUNBUFFERED 1
RUN adduser -D python
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
USER python
ENTRYPOINT ["sh", "runserver.sh"]