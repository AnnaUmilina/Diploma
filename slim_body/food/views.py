from django.shortcuts import render


def index(request):
    return render(request, 'food/index.html')


def diets(request):
    return render(request, 'food/diets.html')


def recipes(request):
    return render(request, 'food/recipes.html')
