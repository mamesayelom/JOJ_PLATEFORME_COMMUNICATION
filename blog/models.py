from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_categorie

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)


    def __str__(self):
        return self.titre


