from django.db import models

class Documentos(models.Model):
    descricao = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.descricao
