from django.db import models
from django.contrib.auth.models import User
from blog.models import Article

# Create your models here.

class Commentaire(models.Model):
    contenu = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='commentaires'
    )

    def __str__(self):
        return self.contenu
    