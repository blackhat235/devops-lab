FROM python:3.11-slim

WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir requests

RUN pip install prometheus_client

CMD ["python", "bot.py"]
