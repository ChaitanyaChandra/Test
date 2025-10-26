FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# RUN useradd -m webhookuser
# USER webhookuser
EXPOSE 443
CMD ["gunicorn", "--certfile=/mnt/certs/tls.crt", "--keyfile=/mnt/certs/tls.key", "-b", "0.0.0.0:443", "index:app"]
