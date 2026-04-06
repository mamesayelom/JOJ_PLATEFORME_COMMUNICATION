from django.shortcuts import get_object_or_404, redirect
from .forms import CommentaireForm
from blog.models import Article
from django.views.generic import UpdateView
from .models import Commentaire
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse


# Create your views here.

def ajout_commentaire(request, id):
    article = get_object_or_404(Article, id=id)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.user = request.user
            commentaire.save()

    return redirect('detail_article', id=article.id)
        

class CommentaireUpdateView(UserPassesTestMixin, UpdateView):
    model = Commentaire
    fields = ['contenu']
    template_name = 'commentaire_edit.html'

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.user
    
    def get_success_url(self):
        # redirige vers la page de l'article du commentaire
        return reverse('detail_article', kwargs={'id': self.object.article.id})