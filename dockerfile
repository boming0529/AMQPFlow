FROM python:3.11-slim

WORKDIR /app

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project files
COPY requirements.txt .
COPY src/ src/
COPY main.py .


CMD ["uv", "run", "python", "main.py"]