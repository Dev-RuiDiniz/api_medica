import os
from pathlib import Path

from dotenv import load_dotenv

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
SECRET_KEY = os.environ.get("SECRET_KEY")

# Use a variável de ambiente carregada para DEBUG (e converte para booleano)
# Ex: DEBUG=True ou DEBUG=1 no ambiente
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "t")

# Use a variável de ambiente carregada para ALLOWED_HOSTS
# Ex: ALLOWED_HOSTS=localhost,127.0.0.1,api.com
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")


# ==============================================================================
# 2. DEFINIÇÃO DA APLICAÇÃO
# ==============================================================================

INSTALLED_APPS = [
    # Core Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",  # Django REST Framework
    # Local apps
    "professionals",  # Seu primeiro app
    "appointments",  # App para gerenciar consultas médicas
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "medical_appointment_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "medical_appointment_api.wsgi.application"


# ==============================================================================
# 3. BANCO DE DADOS (POSTGRESQL - CONFIGURADO VIA DOCKER COMPOSE)
# ==============================================================================

DATABASES = {
    "default": {
        # O Django deve usar o driver PostgreSQL
        "ENGINE": "django.db.backends.postgresql",
        # Variáveis lidas do ambiente (via docker-compose.yml ou .env)
        "NAME": os.environ.get("POSTGRES_NAME"),  # Ex: medical_appointment_db
        "USER": os.environ.get("POSTGRES_USER"),  # Ex: api_user
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),  # Ex: sua_senha
        "HOST": os.environ.get("POSTGRES_HOST"),  # Nome do serviço no Docker: db
        "PORT": os.environ.get("POSTGRES_PORT", 5432),  # Porta padrão do Postgres
    }
}


# ==============================================================================
# 4. VALIDAÇÃO DE SENHA
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==============================================================================
# 5. INTERNACIONALIZAÇÃO
# ==============================================================================

LANGUAGE_CODE = "pt-br"  # Alterado para Português do Brasil

TIME_ZONE = "America/Sao_Paulo"  # Alterado para o fuso horário de São Paulo

USE_I18N = True

USE_TZ = True


# ==============================================================================
# 6. ARQUIVOS ESTÁTICOS E CHAVE PRIMÁRIA PADRÃO
# ==============================================================================

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================================================
# 7. DJANGO REST FRAMEWORK CONFIGURATIONS
# ==============================================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# ==============================================================================
# 8. CORS CONFIGURATIONS
# ==============================================================================

# Se True, permite QUALQUER origem (Use apenas em desenvolvimento inicial)
CORS_ALLOW_ALL_ORIGINS = DEBUG

# Para produção, use a whitelist específica:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Comum para React
    "http://127.0.0.1:3000",
    "http://localhost:5173",  # Comum para Vite
]

# ==============================================================================
# 9. LOGGING CONFIGURATION
# ==============================================================================

# Cria a pasta de logs se ela não existir (útil para o ambiente local)
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file_errors": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "errors.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
        "file_access": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "access.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file_errors"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["file_access", "file_errors"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
