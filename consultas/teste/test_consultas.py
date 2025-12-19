from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone

from profissionais.models import Profissional
from consultas.models import Consulta


class ConsultaAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="123456"
        )

        self.profissional = Profissional.objects.create(
            nome_social="João Lima",
            profissao="Médico",
            endereco="Rua B, 456",
            contato="21988888888"
        )

        self.url = "/api/consultas/"

        self.consulta_data = {
            "data": timezone.now(),
            "profissional": self.profissional.id
        }

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

    
    def test_list_consultas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    def test_create_consulta_authenticated(self):
        self.authenticate()
        response = self.client.post(self.url, self.consulta_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 1)

    
    def test_create_consulta_unauthenticated(self):
        response = self.client.post(self.url, self.consulta_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # ← CORREÇÃO AQUI


    
    def test_create_consulta_invalid_profissional(self):
        self.authenticate()
        invalid_data = {
            "data": timezone.now(),
            "profissional": 999
        }

        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_filter_consultas_by_profissional(self):
        self.authenticate()
        Consulta.objects.create(
            data=timezone.now(),
            profissional=self.profissional
        )

        response = self.client.get(f"{self.url}?profissional={self.profissional.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)