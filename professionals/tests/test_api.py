from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from professionals.models import Professional

class ProfessionalAPITest(APITestCase):
    def setUp(self):
        """Dados iniciais para os testes"""
        self.list_url = reverse('professional-list') # Rota gerada pelo DefaultRouter
        self.professional_data = {
            "name": "Dr. Roberto",
            "profession": "Neurologista",
            "address": "Av. Brasil, 500",
            "contact": "11988887777",
            "registration_number": "CRM/SP 999"
        }

    def test_create_professional_success(self):
        """Garante que é possível criar um profissional via POST"""
        response = self.client.post(self.list_url, self.professional_data, format='json')
        
        # Verifica se retornou 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verifica se o dado foi realmente salvo no banco
        self.assertEqual(Professional.objects.count(), 1)
        self.assertEqual(Professional.objects.get().name, "Dr. Roberto")

    def test_list_professionals(self):
        """Garante que o GET retorna a lista de profissionais cadastrados"""
        # Cria um profissional diretamente no banco primeiro
        Professional.objects.create(**self.professional_data)
        
        response = self.client.get(self.list_url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se a lista retornada tem 1 item
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Dr. Roberto")

    def test_contact_sanitization_in_api(self):
        """Valida se a limpeza do contato funciona via API"""
        data_with_mask = self.professional_data.copy()
        data_with_mask["contact"] = "(11) 98888-7777"
        
        response = self.client.post(self.list_url, data_with_mask, format='json')
        
        # O Serializer deve aceitar e limpar para apenas dígitos
        self.assertEqual(response.data['contact'], "11988887777")