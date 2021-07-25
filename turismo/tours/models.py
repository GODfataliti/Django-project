from django.db import models
from django.contrib.auth.models import AbstractUser   

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10)

class Tour(models.Model):
    nombre=models.CharField(max_length=60)
    dias=models.IntegerField()
    tours=models.Manager()

    def __str__(self):
        return self.nombre

class TourFacade:
    def __init__(self):
        self.tourFactory=Tour.tours
    
    def buscarTours(self):
        return self.tourFactory.all()
    
    def buscarTour(self,id):
        return self.tourFactory.get(id=id)