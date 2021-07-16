#Ruta de la aplicacion

from django.conf.urls import url, re_path
from django.urls import path,include,reverse
from tours import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'tours/',views.HomeToursView.as_view(),name="tours"),
]