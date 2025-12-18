# appointments/models.py
from django.db import models

# Importação usando parênteses (padrão Black/PEP 8)
from professionals.models import (
    Professional
)

class Appointment(models.Model):
    """
    Representa um agendamento de consulta entre um paciente e um profissional.
    """

    # 1. Relacionamento com o Profissional
    # PROTECT: Impede a exclusão do profissional se houver agendamentos vinculados.
    # related_name: Permite acessar os agendamentos a partir do objeto professional.
    professional = models.ForeignKey(
        Professional,
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Profissional",
    )

    # 2. Data e Hora da Consulta
    # DateTimeField armazena tanto a data quanto o horário.
    date = models.DateTimeField(verbose_name="Data e Horário da Consulta")

    # Campos de Auditoria (Boa prática)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        # Ordenar os agendamentos pela data mais próxima por padrão
        ordering = ["date"]

    def __str__(self):
        """Representação amigável do agendamento"""
        # Formata a data para um padrão legível: DD/MM/YYYY HH:MM
        formatted_date = self.date.strftime("%d/%m/%Y %H:%M")
        return f"Consulta com {self.professional.name} em {formatted_date}"
