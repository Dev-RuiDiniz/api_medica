#!/bin/bash

# Encerra o script se algum comando falhar
set -e

echo "--- Aguardando banco de dados... ---"
# Opcional: Aqui você poderia adicionar um check de saúde do DB

echo "--- Aplicando migrações do banco de dados ---"
python manage.py migrate --noinput

echo "--- Coletando arquivos estáticos ---"
python manage.py collectstatic --noinput

# Inicia o servidor conforme o comando passado no Dockerfile ou Docker Compose
echo "--- Iniciando o servidor ---"
exec "$@"