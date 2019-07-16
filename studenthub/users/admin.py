from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import HubUserCreationForm, HubUserChangeForm
from .models import HubUser


class HubUserAdmin(UserAdmin):
    add_form = HubUserCreationForm
    form = HubUserChangeForm
    model = HubUser
    list_display = ['email', 'username', ]


admin.site.register(HubUser, HubUserAdmin)
