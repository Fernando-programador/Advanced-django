from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=150, help_text='nome da empresa')
    
    
    def __str__(self):
        return self.nome
