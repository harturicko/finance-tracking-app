FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "wsgi-install.sh"]