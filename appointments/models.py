from django.db import models
from professionals.models import Professional


class Appointment(models.Model):
    """
    Representa um agendamento de consulta entre um paciente e um profissional.
    """

    professional = models.ForeignKey(
        Professional,
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Profissional",
    )
    date = models.DateTimeField(verbose_name="Data e Horário da Consulta")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ["date"]

    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y %H:%M")
        return f"Consulta com {self.professional.name} em {formatted_date}"