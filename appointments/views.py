from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar agendamentos.
    Permite filtrar consultas por profissional através da URL:
    Exemplo: /api/v1/appointments/?professional_id=1
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset(self):
        """
        Sobrescreve o queryset padrão para permitir filtragem dinâmica.
        """
        # Captura o queryset base (todos os agendamentos)
        queryset = Appointment.objects.all()
        
        # Tenta obter o professional_id dos parâmetros da URL (Query Params)
        professional_id = self.request.query_params.get('professional_id')
        
        if professional_id is not None:
            # Filtra os agendamentos pelo ID do profissional informado
            queryset = queryset.filter(professional_id=professional_id)
            
        return queryset