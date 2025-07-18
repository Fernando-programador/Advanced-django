from django.db import models
from apps.funcionario.models import Funcionario


class RegistroExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.motivo
