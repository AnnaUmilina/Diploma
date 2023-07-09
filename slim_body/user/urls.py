from django.urls import path
from user import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('authorisation/', views.authorisation, name='authorisation'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('account/', views.account, name='account'),
]