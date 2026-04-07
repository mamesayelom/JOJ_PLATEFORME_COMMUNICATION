from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    first_name = forms.CharField(
        required=True,
        label="Prénom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Prénom'
        })
    )

    last_name = forms.CharField(
        required=True,
        label="Nom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom'
        })
    )

    username = forms.CharField(
        required=True,
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Nom d'utilisateur"
        })
    )

    password1 = forms.CharField(
        required=True,
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )

    password2 = forms.CharField(
        required=True,
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie', 'image']

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de l’article'
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Écris ton article...'
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }