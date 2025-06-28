from django.db import models
from apps.funcionario.models import Funcionario

class Documentos(models.Model):
    descricao = models.CharField(max_length=255)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.descricao
