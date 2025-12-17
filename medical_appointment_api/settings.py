import os
from dotenv import load_dotenv
from pathlib import Path

# ==============================================================================
# 1. SETUP INICIAL E VARIÁVEIS DE AMBIENTE
# ==============================================================================

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis de ambiente do arquivo .env (se existir)
# As variáveis definidas no docker-compose.yml têm precedência,
# mas esta linha garante que as variáveis existam no ambiente local.
load_dotenv()


# Use as variáveis de ambiente carregadas
SECRET_KEY = os.environ.get('SECRET_KEY')

# Use a variável de ambiente carregada para DEBUG (e converte para booleano)
# Ex: DEBUG=True ou DEBUG=1 no ambiente
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')

# Use a variável de ambiente carregada para ALLOWED_HOSTS
# Ex: ALLOWED_HOSTS=localhost,127.0.0.1,api.com
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# ==============================================================================
# 2. DEFINIÇÃO DA APLICAÇÃO
# ==============================================================================

INSTALLED_APPS = [
    # Core Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework', # Django REST Framework
    
    # Local apps
    'professionals', # Seu primeiro app
    'appointments',  # App para gerenciar consultas médicas
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medical_appointment_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'medical_appointment_api.wsgi.application'


# ==============================================================================
# 3. BANCO DE DADOS (POSTGRESQL - CONFIGURADO VIA DOCKER COMPOSE)
# ==============================================================================

DATABASES = {
    'default': {
        # O Django deve usar o driver PostgreSQL
        'ENGINE': 'django.db.backends.postgresql',
        
        # Variáveis lidas do ambiente (via docker-compose.yml ou .env)
        'NAME': os.environ.get('POSTGRES_NAME'),     # Ex: medical_appointment_db
        'USER': os.environ.get('POSTGRES_USER'),     # Ex: api_user
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'), # Ex: sua_senha
        'HOST': os.environ.get('POSTGRES_HOST'),     # Nome do serviço no Docker: db
        'PORT': os.environ.get('POSTGRES_PORT', 5432), # Porta padrão do Postgres
    }
}


# ==============================================================================
# 4. VALIDAÇÃO DE SENHA
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==============================================================================
# 5. INTERNACIONALIZAÇÃO
# ==============================================================================

LANGUAGE_CODE = 'pt-br' # Alterado para Português do Brasil

TIME_ZONE = 'America/Sao_Paulo' # Alterado para o fuso horário de São Paulo

USE_I18N = True

USE_TZ = True


# ==============================================================================
# 6. ARQUIVOS ESTÁTICOS E CHAVE PRIMÁRIA PADRÃO
# ==============================================================================

STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'