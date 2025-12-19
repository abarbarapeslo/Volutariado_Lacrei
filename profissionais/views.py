from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profissional
from .serializers import ProfissionalSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProfissionalViewSet(ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permissaion_classes = [IsAuthenticatedOrReadOnly] #permissão autenticada