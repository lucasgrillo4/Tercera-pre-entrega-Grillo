from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente=models.CharField(max_length=40)
    nCliente = models.IntegerField()
    email= models.EmailField()
    def __str__(self):
        return self.cliente

class Central(models.Model):
    nombreCentral= models.CharField(max_length=30)
    cantidadContratos= models.IntegerField()
    def __str__(self):
        return self.nombreCentral

class Contrato(models.Model):
    clienteNombre= models.CharField(max_length=30)
    tipoContrato= models.CharField(max_length=30)
    numContrato = models.IntegerField()
    def __str__(self):
        return f"Cliente: {self.clienteNombre} - Contrato {self.numContrato}"

    