# Create your models here.
from django.db import models


class Professional(models.Model):
    """
    Modelo representa um profissional de saúde, como médicos,
    enfermeiros ou fisioterapeutas.
    """

    # 1. Nome Social/Nome Completo
    # Não pode ser nulo (obrigatório) e tem um limite de 255 caracteres.
    name = models.CharField(
        max_length=255, verbose_name="Nome Completo / Social", null=False, blank=False
    )

    # 2. Profissão
    # Campo obrigatório para definir a área de atuação.
    profession = models.CharField(
        max_length=100, verbose_name="Profissão", null=False, blank=False
    )

    # 3. Endereço (Pode ser um campo longo para flexibilidade)
    # Considerado obrigatório no cadastro inicial.
    address = models.CharField(
        max_length=255, verbose_name="Endereço", null=False, blank=False
    )

    # 4. Contato (Telefone/Celular)
    # Campo obrigatório para o contato principal.
    contact = models.CharField(
        max_length=20,
        verbose_name="Contato (Telefone/Celular)",
        null=False,
        blank=False,
    )

    # Adicionando um campo opcional para registro/CRM (Boa Prática)
    # Pode ser nulo/em branco
    registration_number = models.CharField(
        max_length=50,
        verbose_name="Registro (CRM/CREFITO/etc.)",
        null=True,
        blank=True,
        unique=True,  # Garante que cada registro seja único
    )

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
        # Ordenar por nome por padrão
        ordering = ["name"]

    def __str__(self):
        """Retorna o nome do profissional para representação amigável."""
        return f"{self.name} ({self.profession})"


#
