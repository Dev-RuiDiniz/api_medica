from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Appointment.
    
    Exibe o ID do profissional para operações de escrita (POST/PUT)
    e o nome do profissional apenas para leitura.
    """
    
    # ReadOnlyField: Busca o atributo 'name' através da ForeignKey 'professional'.
    # O 'source' permite navegar no relacionamento: do agendamento para o profissional.
    professional_name = serializers.ReadOnlyField(source='professional.name')

    class Meta:
        model = Appointment
        fields = [
            'id', 
            'professional',      # ID do profissional (obrigatório no POST)
            'professional_name', # Nome social (retornado apenas no GET)
            'date', 
            'created_at', 
            'updated_at'
        ]
        
    def validate_date(self, value):
        """
        Uma pequena validação extra: não permitir agendamentos no passado.
        """
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser no passado.")
        return value