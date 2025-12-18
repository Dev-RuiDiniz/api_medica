from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from professionals.models import Professional
from django.urls import reverse

class ProfessionalAPITest(APITestCase):
    def setUp(self):
        # 1. Autenticação
        self.user = User.objects.create_user(username="testadmin", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # 2. URL (Certifique-se que o nome no urls.py é 'professional-list')
        # Se não tiver nome na rota, use a string direta: "/api/professionals/"
        try:
            self.list_url = reverse("professional-list")
        except:
            self.list_url = "/api/professionals/"

        # 3. Dados (Ajustados para os campos em PORTUGUÊS do seu modelo)
        self.professional_data = {
            "nome": "Dra. Ana",
            "especialidade": "Pediatra",
            "crm": "123456",
            "email": "ana@teste.com",
            "contato": "11988887777" 
        }

    def test_create_professional_success(self):
        response = self.client.post(self.list_url, self.professional_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_professionals(self):
        Professional.objects.create(**self.professional_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_contact_sanitization_in_api(self):
        # Testa se a limpeza que criamos no Serializer está funcionando
        data_with_mask = self.professional_data.copy()
        data_with_mask["contato"] = "(11) 98888-7777"
        response = self.client.post(self.list_url, data_with_mask, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # O banco deve salvar apenas os números
        self.assertEqual(response.data["contato"], "11988887777")