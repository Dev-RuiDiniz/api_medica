# professionals/urls.py

from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet

# 1. Instancia o DefaultRouter. Ele cuidará das URLs
router = DefaultRouter()

# 2. Registra o ProfessionalViewSet. Isso gera as URLs CRUD:
#    - professionals/ (GET, POST)
#    - professionals/{pk}/ (GET, PUT, PATCH, DELETE)
router.register(r'professionals', ProfessionalViewSet)

# 3. Exporta as URLs geradas
urlpatterns = router.urls