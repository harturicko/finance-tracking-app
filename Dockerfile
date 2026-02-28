FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add gcc musl-dev apache2 apache2-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mod_wsgi
RUN adduser -D -H wsgi

COPY . .

CMD ["mod_wsgi-express", "start-server", "wsgi", "--user", "wsgi", "--group", "wsgi", "--port", "5000", "--host", "0.0.0.0", "--application-type", "module"]