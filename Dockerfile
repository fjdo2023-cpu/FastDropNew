
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Porta usada pelo Render (ele sobrescreve se quiser)
ENV PORT=10000

# Gunicorn em modo produção
CMD gunicorn -b 0.0.0.0:$PORT app:app
