FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask gunicorn
CMD ["gunicorn", "--certfile=tls.crt", "--keyfile=tls.key", "-b", "0.0.0.0:443", "index:app"]
