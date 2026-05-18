FROM python:3.14.5-alpine3.23 AS builder
USER root
RUN adduser -u 1000 webhookuser -D
WORKDIR /app
COPY --chown=webhookuser:webhookuser requirements.txt /app
COPY --chown=webhookuser:webhookuser ./routers/*.py /app/routers/
copy --chown=webhookuser:webhookuser index.py /app
RUN pip3 install --no-cache-dir -r requirements.txt --target=/install
ENV DEBUG="true"

FROM FROM python:3.14.5-alpine3.23  
WORKDIR /app
COPY --chown=webhookuser:webhookuser --from=builder /install /usr/lib/python3.14/site-packages
COPY --chown=webhookuser:webhookuser --from=builder /app /app
USER webhookuser
EXPOSE 8080
CMD [ "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "index:app", "--ssl-keyfile", "/app/ssl/tls.key", "--ssl-certfile", "/app/ssl/tls.crt" ]

