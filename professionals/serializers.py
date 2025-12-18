# professionals/serializers.py

from rest_framework import serializers

from .models import Professional


class ProfessionalSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Professional, incluindo validação customizada.
    """

    class Meta:
        model = Professional
        fields = "__all__"

    def validate_contact(self, value):
        """
        Valida e sanitiza o campo de contato.
        1. Remove caracteres não numéricos.
        2. Verifica o tamanho (mínimo de 10 dígitos para DDD + 8 dígitos).
        3. Garante que o campo contém apenas dígitos após a sanitização.
        """
        # 1. Sanitização: Remove espaços, traços, parênteses e pontos
        sanitized_contact = "".join(filter(str.isdigit, value))

        # 2. Validação de Tamanho
        min_length = 10  # Ex: (XX) XXXX-XXXX
        max_length = 11  # Ex: (XX) 9XXXX-XXXX (com nono dígito)

        if not (min_length <= len(sanitized_contact) <= max_length):
            # Quebramos a string para não ultrapassar o limite de caracteres da linha
            raise serializers.ValidationError(
                f"O campo Contato deve ter entre {min_length} e "
                f"{max_length} dígitos (após remover formatação)."
            )

        # 3. Garante que o campo contém apenas dígitos
        if not sanitized_contact.isdigit():
            raise serializers.ValidationError(
                "O campo Contato deve conter apenas caracteres numéricos."
            )

        return sanitized_contact