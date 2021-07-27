from django.test import TestCase
from .models import Tour,TourFacade

# Create your tests here.

class TourTestCase(TestCase):

    def setUp(self):
        '''Esta clase define la variables generales'''
        self.nombre="PN La Campana"
        self.dias=1
        self.tour= Tour(nombre=self.nombre,dias=self.dias)
    
    def test_creacion_de_tour(self):
        '''Test de creacion de un tour'''
        old_count=Tour.tours.count()
        self.tour.save()
        new_count=Tour.tours.count()
        self.assertNotEqual(old_count,new_count)