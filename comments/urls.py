
from django.urls import path
from . import views
from .views import CommentaireUpdateView,CommentaireDeleteView

urlpatterns = [
     path('article/<int:id>/commenter/', views.ajout_commentaire, name='ajouter_commentaire'),
     path('commentaire/<int:pk>/edit/', CommentaireUpdateView.as_view(), name='commentaire_edit'),
     path('commentaire/<int:pk>/delete/', CommentaireDeleteView.as_view(), name='commentaire_delete'),
]