from django.test import TestCase

from professionals.models import Professional


class ProfessionalModelTest(TestCase):
    def setUp(self):
        """Configura os dados iniciais para o teste"""
        self.professional = Professional.objects.create(
            name="Dra. Ana",
            profession="Pediatra",
            address="Rua A, 123",
            contact="11999999999",
            registration_number="CRM123",
        )

    def test_professional_str(self):
        """Valida se o método __str__ do modelo retorna o nome correto"""
        self.assertEqual(str(self.professional), "Dra. Ana")
