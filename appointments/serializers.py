from django.utils import timezone
from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    professional_name = serializers.ReadOnlyField(source="professional.name")

    class Meta:
        model = Appointment
        fields = [
            "id",
            "professional",
            "professional_name",
            "date",
            "created_at",
            "updated_at",
        ]

    def validate_date(self, value):
        """
        Validação de segurança: impede agendamentos em datas retroativas.
        """
        if value < timezone.now():
            # Quebramos a string em duas para respeitar o limite de 88 caracteres
            raise serializers.ValidationError(
                "Não é possível agendar uma consulta para uma "
                "data ou horário no passado."
            )

        return value