from django.db import models
from django.contrib.auth.models import AbstractUser   

# Create your models here.
class Usuario(AbstractUser):
    rut = models.CharField(max_length=10)


class Tour:
    def __init__(self,id,nombre,dias):
        self.id=id
        self.nombre=nombre
        self.dias=dias


class TourFactory:
    def __init__(self):
        self.tours=[]
        self.tours.append(Tour(1,"Valle de la Luna"))
        self.tours.append(Tour(2,"Torres del Paine"))
    
    def obtener_tours(self):
        return self.tours