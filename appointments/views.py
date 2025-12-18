from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.exceptions import ValidationError

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar agendamentos.
    Permite filtrar consultas por profissional através da URL:
    Exemplo: /api/v1/appointments/?professional_id=1
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset(self):
        queryset = Appointment.objects.all()
        professional_id = self.request.query_params.get('professional_id')
        
        if professional_id:
            # Validação de Tipo: Garante que é um número antes de chegar ao banco
            if not professional_id.isdigit():
                raise ValidationError({"professional_id": "Este campo deve ser um número inteiro."})
                
            queryset = queryset.filter(professional_id=professional_id)
            
        return queryset