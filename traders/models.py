from django.db import models


class Traders(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=80)
    celular = models.CharField(max_length=15)
    email = models.CharField(max_length=150)

