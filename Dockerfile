# 1. IMAGEM BASE
# Usamos uma imagem oficial do Python, baseada em Debian, que inclui o Poetry
# e otimiza o tamanho final da imagem.
FROM python:3.11-slim

# 2. VARIÁVEIS DE AMBIENTE
# Evita que Python grave arquivos .pyc no disco (performance)
ENV PYTHONDONTWRITEBYTECODE 1 
# Não armazena saída em buffer (útil para logs em containers)
ENV PYTHONUNBUFFERED 1

# 3. INSTALAÇÃO DO POETRY (Se a imagem 'slim' não o incluir por padrão)
# Geralmente, imagens 'slim' não incluem o Poetry, então instalamos ele via pip.
# A versão 1.7.1 é a mais estável e recente na época.
RUN pip install poetry==1.7.1

# 4. WORKING DIRECTORY
# Define o diretório de trabalho padrão dentro do container.
WORKDIR /usr/src/app

# 5. CÓPIA DOS ARQUIVOS DE DEPENDÊNCIAS
# Copiamos apenas os arquivos necessários para instalar as dependências
# Isso permite que o Docker faça cache nesta camada (melhorando o build)
COPY pyproject.toml poetry.lock /usr/src/app/

# 6. INSTALAÇÃO DAS DEPENDÊNCIAS
# O Poetry instala todas as dependências listadas no pyproject.toml
# e travadas no poetry.lock
RUN poetry install --no-root