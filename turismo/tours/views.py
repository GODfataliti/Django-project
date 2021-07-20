from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, TemplateView
from .models import Tour,TourFactory

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwars):
        return render(request, "index.html",context=None)

class HomeToursView(TemplateView):
    def get(self, request, **kwars):
        tourFactory=TourFactory()
        return render(request,"tours.html",{"tours": tourFactory.tours}) # "tours" es el nombre de la variable a iterar en el tours.html {% for tour in tours %}

class DetalleTourView(TemplateView):
    def get(self, request, **kwars):
        id=int(kwars["id"])
        tourFactory=TourFactory()
        return render(request, 'tour.html',{"tour": tourFactory.getTour(id)})