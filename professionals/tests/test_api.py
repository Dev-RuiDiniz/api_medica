from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from professionals.models import Professional
from django.urls import reverse

class ProfessionalAPITest(APITestCase):
    def setUp(self):
        # 1. Autenticação (Necessário se a sua View tiver permissões)
        self.user = User.objects.create_user(username="testadmin", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # 2. URL da API
        self.list_url = "/api/v1/professionals/"

        # 3. Dados (Sincronizados com o seu models.py)
        self.professional_data = {
            "name": "Dra. Ana Silva",
            "profession": "Pediatra",
            "address": "Rua das Flores, 123",
            "contact": "11988887777",
            "registration_number": "CRM/SP 123456"
        }

    def test_create_professional_success(self):
        """Garante que é possível criar um profissional via POST"""
        response = self.client.post(self.list_url, self.professional_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_professionals(self):
        """Garante que o GET retorna a lista de profissionais cadastrados"""
        Professional.objects.create(**self.professional_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o item criado está na lista
        self.assertEqual(len(response.data), 1)

    def test_contact_sanitization_in_api(self):
        """Valida se a limpeza do contato funciona via API (removendo máscaras)"""
        data_with_mask = self.professional_data.copy()
        data_with_mask["contact"] = "(11) 98888-7777"
        data_with_mask["registration_number"] = "CRM/SP 654321" # Unique constraint
        
        response = self.client.post(self.list_url, data_with_mask, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # O valor retornado deve ser apenas números (conforme sua lógica de validação no serializer)
        self.assertEqual(response.data["contact"], "11988887777")