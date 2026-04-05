from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_article,name='liste_article'),
    path('inscription/',views.inscription,name='inscription'),
  
]