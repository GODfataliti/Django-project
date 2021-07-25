from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, TemplateView
from .models import Tour,TourFacade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView,LoginRequiredMixin):
    def get(self, request, **kwars):
        return render(request, "index.html",context=None)

class HomeToursView(TemplateView,LoginRequiredMixin):
    def get(self, request, **kwars):
        tourFacade=TourFacade()
        return render(request,"tours.html",{"tours": tourFacade.buscarTours}) # "tours" es el nombre de la variable a iterar en el tours.html {% for tour in tours %}

class DetalleTourView(TemplateView):
    def get(self, request, **kwars):
        id=int(kwars["id"])
        tourFacade=TourFacade()
        return render(request, 'tour.html',{"tour": tourFacade.buscarTour(id)})

class TourCreate(CreateView):
    model=Tour
    template_name='./tour_form.html'
    fields='__all__'

class TourUpdate(UpdateView):
    model=Tour
    template_name='./tour_form.html'
    fields=['nombre','dias']

class TourDelete(DeleteView):
    model=Tour
    template_name='./tour_confirm_delete.html'
    success_url=reverse_lazy('tours')