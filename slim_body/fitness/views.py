from django.shortcuts import render


def fitness(request):
    return render(request, 'fitness/fitness.html')
