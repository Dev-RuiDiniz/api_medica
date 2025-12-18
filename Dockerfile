# ==========================================
# ESTÁGIO 1: Builder (Ambiente de Compilação)
# ==========================================
FROM python:3.12-slim AS builder

# Impede que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=true

WORKDIR /app

# Instala dependências de sistema necessárias para compilar pacotes (como psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN pip install poetry

# Copia apenas os arquivos de dependências primeiro (otimiza cache)
COPY pyproject.toml poetry.lock ./

# Instala as dependências (cria a pasta .venv dentro de /app)
RUN poetry install --no-root --only main

# ==========================================
# ESTÁGIO 2: Runtime (Imagem Final de Produção)
# ==========================================
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Instala apenas a biblioteca runtime do Postgres (necessária para rodar, não para compilar)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copia o ambiente virtual (Python + Bibliotecas) do estágio builder
COPY --from=builder /app/.venv /app/.venv

# Copia o código fonte do projeto
COPY . .

# Expõe a porta do Django
EXPOSE 8000

# O comando de execução permanece o mesmo, mas agora usando o binário do venv
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]