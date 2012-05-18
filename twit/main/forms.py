from django import forms
from main.models import Perfil, Tweet


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet


class AddTwettForm(forms.ModelForm):
    class Meta:
        model = Tweet
