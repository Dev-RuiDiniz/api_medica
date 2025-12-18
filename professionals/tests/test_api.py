from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from professionals.models import Professional

class ProfessionalAPITest(APITestCase):
    def setUp(self):
        # Cria um usuário e autentica o cliente para evitar o erro 401
        self.user = User.objects.create_user(username="admin", password="password")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.professional_data = {
            "name": "Dra. Ana",
            "specialty": "Pediatra",
            "crm": "123456",
            "email": "ana@teste.com",
            "phone": "11988887777" # Verifique se o nome é 'phone' ou 'telefone'
        }

    def test_create_professional_success(self):
        response = self.client.post("/api/professionals/", self.professional_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_professionals(self):
        Professional.objects.create(**self.professional_data)
        response = self.client.get("/api/professionals/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_sanitization_in_api(self):
        """Valida se a limpeza do contato funciona via API"""
        data_with_mask = self.professional_data.copy()
        data_with_mask["contact"] = "(11) 98888-7777"

        response = self.client.post(self.list_url, data_with_mask, format="json")

        # O Serializer deve aceitar e limpar para apenas dígitos
        self.assertEqual(response.data["contact"], "11988887777")

    def test_create_professional_missing_name_fails(self):
        """
        Garante que a API rejeita a criação de um profissional sem o campo 'name'.
        Deve retornar Status 400 Bad Request.
        """
        # Preparamos os dados omitindo deliberadamente o campo 'name'
        invalid_data = {
            "profession": "Dentista",
            "address": "Rua Sem Nome, 0",
            "contact": "11912345678",
            "registration_number": "CRO123",
        }

        response = self.client.post(self.list_url, invalid_data, format="json")

        # 1. Verifica se o status code é 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 2. Verifica se a mensagem de erro aponta para o campo 'name'
        self.assertIn("name", response.data)
        self.assertEqual(response.data["name"][0], "Este campo é obrigatório.")

        # 3. Garante que nada foi criado no banco de dados
        self.assertEqual(Professional.objects.count(), 0)
