from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SecurityAccessTest(APITestCase):
    def setUp(self):
        # Rota para listagem de profissionais
        self.url = reverse('professional-list')

    def test_access_denied_without_token(self):
        """
        Garante que qualquer requisição sem o Token de autorização
        seja rejeitada com status 401 Unauthorized.
        """
        # Fazemos a requisição sem configurar nenhum header de autorização
        response = self.client.get(self.url)
        
        # O DRF deve retornar 401 (ou 403 dependendo da configuração, 
        # mas com TokenAuthentication o padrão para falta de credencial é 401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Opcional: Validar se a mensagem de erro está presente
        self.assertIn('detail', response.data)
        self.assertEqual(
            response.data['detail'], 
            "As credenciais de autenticação não foram fornecidas."
        )

    def test_access_denied_with_invalid_token(self):
        """
        Garante que um Token malformado ou inexistente também seja rejeitado.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token token_invalido_123')
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)