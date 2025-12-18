#!/bin/bash
set -e

echo "--- Aguardando banco de dados... ---"
echo "--- Aplicando migrações ---"
python manage.py migrate --noinput

echo "--- Coletando arquivos estáticos ---"
python manage.py collectstatic --noinput

echo "--- Iniciando o servidor ---"
exec "$@"