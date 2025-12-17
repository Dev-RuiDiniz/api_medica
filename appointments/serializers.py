from rest_framework import serializers
from django.utils import timezone # Importação essencial para lidar com fusos horários
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    professional_name = serializers.ReadOnlyField(source='professional.name')

    class Meta:
        model = Appointment
        fields = [
            'id', 
            'professional', 
            'professional_name', 
            'date', 
            'created_at', 
            'updated_at'
        ]

    def validate_date(self, value):
        """
        Validação de segurança: impede agendamentos em datas retroativas.
        """
        # Verifica se a data enviada (value) é menor que o momento atual
        if value < timezone.now():
            raise serializers.ValidationError(
                "Não é possível agendar uma consulta para uma data ou horário no passado."
            )
        
        # Opcional: Validar se a consulta é agendada com pelo menos 30 min de antecedência
        # if value < timezone.now() + timezone.timedelta(minutes=30):
        #     raise serializers.ValidationError("Consultas devem ser agendadas com 30 min de antecedência.")

        return value