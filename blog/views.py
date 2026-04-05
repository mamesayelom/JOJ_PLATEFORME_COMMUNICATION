from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,ArticleForm
from .models import Article

# Create your views here.

def liste_article(request):
    articles= Article.objects.all()
    contexte={
        'articles':articles
    }
    return render(request,'liste_articles.html',contexte)

def detail_article(request,id):
    article=get_object_or_404(Article, id=id)
    contexte={
        'article':article
    }
    return render(request,'detail_article.html',contexte)

def ajouter_articles(request):
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article = form.save(commit=False)  # cree un objet mais ne sauvegarde pas encore dans la bd
            article.user = request.user        # on assigne l'utilisateur connecté
            article.save()                     # maintenant on sauvegarde
            return redirect('liste_article')  
    else:
        form = ArticleForm()
    return render(request, 'ajouter_articles.html', {'form': form})

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/inscription.html', {'form': form})
