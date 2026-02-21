FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir mem0ai fastapi uvicorn

EXPOSE 8000

CMD ["python", "-m", "mem0.api.server"]
