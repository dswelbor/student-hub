from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import HubUserCreationForm, HubUserChangeForm
from .models import HubUser


class HubUserAdmin(UserAdmin):
    """
    Class extends django's existing UserAdmin and adds additional fields defined
    in custom user Model HubUser
    """
    add_form = HubUserCreationForm
    form = HubUserChangeForm
    model = HubUser
    # Defines fields to use in user admin pages
    fieldsets = (
                    ('User Profile', {'fields': ('alias', 'is_private')}),
                ) + UserAdmin.fieldsets
    list_display = ['username', 'alias', 'is_superuser']


admin.site.register(HubUser, HubUserAdmin)
