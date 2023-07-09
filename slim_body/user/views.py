from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def authorisation(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'user/authorisation.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('account')
    else:
        return render(request, 'user/authorisation.html', {'form': AuthenticationForm()})


def registration(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account')
            except IntegrityError:
                return render(request, 'user/registration.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует'})
        else:
            return render(request, 'user/registration.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'})
    else:
        return render(request, 'user/registration.html', {'form': UserCreationForm()})


@login_required
def account(request):
    return render(request, 'user/account.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
