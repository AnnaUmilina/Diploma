from django.shortcuts import render
from .models import Articles


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
