from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import HubUser


class HubUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = HubUser
        fields = ('username', 'email')


class HubUserChangeForm(UserChangeForm):

    class Meta:
        model = HubUser
        fields = ('username', 'email')
