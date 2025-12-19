from django.db import models

from profissionais.models import Profissional

# Create your models here.
class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name="consultas"
    )

def __str__(self):
    return f"{self.profissional.nome_social} - {self.data}"
