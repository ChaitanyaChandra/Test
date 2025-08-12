FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask gunicorn
CMD ["gunicorn", "--certfile=/mnt/certs/tls.crt", "--keyfile=/mnt/certs/tls.key", "-b", "0.0.0.0:443", "index:app"]
