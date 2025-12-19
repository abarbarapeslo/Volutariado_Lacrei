from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Consulta
from .serializers import ConsultaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permissaon_class = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        profissional_id = self.request.query_params.get('profissional')

        if profissional_id:
            queryset = queryset.filter(profissional_id=profissional_id)

        return queryset