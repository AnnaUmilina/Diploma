from django.shortcuts import render, get_object_or_404,redirect
from .models import Articles
from .forms import ArticlesForm


def index(request):
    articles = Articles.objects.order_by("-date")
    context = {
        'articles': articles,
    }
    return render(request, 'food/index.html', context)


def diets(request):
    return render(request, 'food/diets.html')


def recipes(request):
    return render(request, 'food/recipes.html')


def articles(request):
    return render(request, 'food/articles.html')


def detail(request, id):
    post = get_object_or_404(Articles, id=id)
    return render(request, 'food/detail.html', {'post': post})


def create_article(request):
    form = ArticlesForm()
    if request.method =='POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        return render(request, 'food/user_article.html', {'form': form})
