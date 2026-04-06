from django.shortcuts import get_object_or_404, redirect
from .forms import CommentaireForm
from blog.models import Article
from django.views.generic import UpdateView,DeleteView
from .models import Commentaire
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
#signal qui est envoyé après qu’un objet a été sauvegardé dans la base de données.
from django.db.models.signals import post_save
#décorateur pour attacher une fonction à un signal.
from django.dispatch import receiver
#fonction Django pour envoyer un mail
from django.core.mail import send_mail

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
    #Je veux modifier un objet de type Commentaire donc django sait quoi récupérer (get_object())
    model = Commentaire
    fields = ['contenu']
    template_name = 'commentaire_edit.html'

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.user
    
    def get_success_url(self):
        # redirige vers la page de l'article du commentaire
        return reverse('detail_article', kwargs={'id': self.object.article.id})

class CommentaireDeleteView(UserPassesTestMixin, DeleteView):
    #Je veux supprimer un objet de type Commentaire
    model = Commentaire

    def test_func(self):
        #récupère le commentaire à supprimer
        commentaire = self.get_object()
        return self.request.user == commentaire.user
    
    def get_success_url(self):
        return reverse('detail_article', kwargs={'id': self.object.article.id})
    

# Cette fonction sera appelée automatiquement à chaque fois qu'un objet Commentaire est créé
@receiver(post_save, sender=Commentaire)
def notifier_admin(sender, instance, created, **kwargs):
    """
    Notifie l'administrateur par email lorsqu'un nouveau commentaire est ajouté.
    
    Arguments :
    - sender : le modèle qui envoie le signal (ici Commentaire)
    - instance : l'objet Commentaire qui vient d'être créé
    - created : True si c'est un nouveau commentaire, False si c'est une mise à jour
    - kwargs : autres informations fournies par le signal
    """
    
    # On ne s'intéresse qu'aux nouveaux commentaires
    if created:
        commentaire = instance  # l'objet Commentaire créé
        article = commentaire.article  # l'article associé à ce commentaire
        
        # Générer un lien vers la page détail de l'article
        # reverse('nom_de_la_vue', kwargs={'id': article.id}) renvoie l'URL correspondante
        lien_article = reverse('detail_article', kwargs={'id': article.id})
        
        # Préparer le contenu du mail
        sujet = f"Nouveau commentaire sur l'article : {article.titre}"
        message = (
            f"Un nouveau commentaire a été ajouté par {commentaire.user.username}.\n\n"
            f"Texte du commentaire :\n{commentaire.contenu}\n\n"
            f"Voir l'article ici : http://127.0.0.1:8000{lien_article}"
        )
        
        # Envoi du mail
        send_mail(
            subject=sujet,
            message=message,
            from_email='noreply@example.com',
            recipient_list=['admin@example.com'],
            fail_silently=True  # en dev, ça empêche l'erreur si le mail ne peut pas partir
        )