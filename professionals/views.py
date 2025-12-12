from rest_framework import viewsets
from .models import Professional
from .serializers import ProfessionalSerializer

class ProfessionalViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Professional.
    
    Herda de ModelViewSet, fornecendo as ações CRUD prontas:
    - GET /api/v1/professionals/ (Listar)
    - GET /api/v1/professionals/{pk}/ (Detalhe)
    - POST /api/v1/professionals/ (Criar)
    - PUT/PATCH /api/v1/professionals/{pk}/ (Atualizar)
    - DELETE /api/v1/professionals/{pk}/ (Deletar)
    """
    
    # Define qual Serializer será usado para transformar dados entre 
    # Python (Modelo) e JSON (API).
    serializer_class = ProfessionalSerializer
    
    # Define o conjunto de objetos (dados) que esta view manipulará.
    # Usar .all() garante que todos os profissionais estarão disponíveis para a ViewSet.
    queryset = Professional.objects.all()