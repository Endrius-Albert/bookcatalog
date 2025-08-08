FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y netcat-traditional gcc libpq-dev dos2unix && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh && dos2unix /app/entrypoint.sh || true

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
