
from django.urls import path
from . import views
from .views import CommentaireUpdateView

urlpatterns = [
     path('article/<int:id>/commenter/', views.ajout_commentaire, name='ajouter_commentaire'),
     path('commentaire/<int:pk>/edit/', CommentaireUpdateView.as_view(), name='commentaire_edit')
]