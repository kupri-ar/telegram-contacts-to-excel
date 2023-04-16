FROM python:3.9-slim-buster

WORKDIR /app

COPY .env .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "svc/main.py" ]