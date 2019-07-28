from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import HubUser


# TODO: Properly implement HubUser Django Forms
class HubUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = HubUser
        fields = ('username', 'email', 'alias', 'is_private')


class HubUserChangeForm(UserChangeForm):

    class Meta:
        model = HubUser
        fields = ('username', 'email', 'alias', 'is_private')
