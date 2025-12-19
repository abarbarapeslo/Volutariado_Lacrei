from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from profissionais.models import Profissional


class ProfissionalAPITestCase(APITestCase):

    def setUp(self):
        # Usuário autenticado
        self.user = User.objects.create_user(
            username="testuser",
            password="123456"
        )

        # Endpoint base
        self.url = "/api/profissionais/"

        # Dados válidos
        self.profissional_data = {
            "nome_social": "Maria Silva",
            "profissao": "Psicóloga",
            "endereco": "Rua A, 123",
            "contato": "21999999999"
        }

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

    
    def test_list_profissionais(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    def test_create_profissional_authenticated(self):
        self.authenticate()
        response = self.client.post(self.url, self.profissional_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(), 1)

    
    def test_create_profissional_unauthenticated(self):
        response = self.client.post(self.url, self.profissional_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_create_profissional_invalid_data(self):
        self.authenticate()
        invalid_data = self.profissional_data.copy()
        invalid_data.pop("nome_social")

        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)