from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'form-control rounded-4',
                'rows': 2,
                'placeholder': 'Écris ton commentaire ici...'
            })
        }
        