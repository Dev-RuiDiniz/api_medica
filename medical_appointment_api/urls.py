from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views  # <-- Importe isso

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("professionals.urls")),
    path("api/v1/", include("appointments.urls")),
    # Endpoint para login: envia username/password e recebe o Token
    path("api-token-auth/", views.obtain_auth_token),
]
