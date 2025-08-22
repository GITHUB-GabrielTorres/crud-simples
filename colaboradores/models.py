from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.email}'
