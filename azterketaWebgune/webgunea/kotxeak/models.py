from django.db import models

# Create your models here.
class Pertsona(models.Model):
  izena = models.CharField(max_length=255)
  tlf = models.FloatField()

class Kotxea(models.Model):
  izena = models.CharField(max_length=255)
  prezioa = models.FloatField()
  
class Alokairua(models.Model):
  alokatuData= models.DateField()
  aamaieraData= models.DateField()
  alokatzailea = models.ForeignKey(Pertsona,on_delete = models.CASCADE, null = True)
  kotxea = models.ForeignKey(Kotxea,on_delete = models.CASCADE, null = True)