from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_article,name='liste_article'),
    path('inscription/',views.inscription,name='inscription'),
    path('detail/<int:id>/article/', views.detail_article,name='detail_article'),
    path('ajouter/article/',views.ajouter_articles,name='ajouter_article')
  
]