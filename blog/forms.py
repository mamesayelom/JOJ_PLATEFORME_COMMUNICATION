from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nom")
    last_name = forms.CharField(required=True, label="Prénom")
    username = forms.CharField(required=True, label="Nom d'utilisateur")
    password1 = forms.CharField(required=True, label="Mot de pass")
    password2 = forms.CharField(required=True, label="Confirmer")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']