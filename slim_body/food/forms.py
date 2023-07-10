from django.forms import ModelForm
from .models import Articles
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'topics', 'image', 'description']
        widgets={'topics': forms.CheckboxSelectMultiple()}

