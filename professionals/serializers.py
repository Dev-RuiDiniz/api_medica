# professionals/serializers.py

from rest_framework import serializers
from .models import Professional

class ProfessionalSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Professional.
    
    Ele define como os dados do modelo Professional serão:
    1. Convertidos em JSON (saída da API - GET).
    2. Convertidos de JSON para um objeto Python (entrada da API - POST/PUT).
    """
    class Meta:
        model = Professional
        # Utilizamos '__all__' para incluir todos os campos definidos no modelo Professional.
        # Alternativamente, poderíamos listar os campos explicitamente: 
        # fields = ['id', 'name', 'profession', 'address', 'contact', 'registration_number']
        fields = '__all__'