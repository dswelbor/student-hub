from django.db import models
from django.contrib.auth.models import AbstractUser


class HubUser(AbstractUser):
    """
    Custom User model that adds additional fields for isPrivate and alias information
    """
    # Add isPrivate field
    is_private = models.BooleanField(default=True)
    # Add alias field
    # Null is allowed as field can be blank and must be unique - prevents constraint exceptions
    alias = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def get_alias(self):
        """Simple getter function to return the user alias."""
        # User has defined alias
        if self.alias:
            return self.alias
        # User has not defined alias
        elif self.get_full_name():
            return self.get_full_name()
        # No valid alias or full name
        else:
            return 'Anonymous'

    def get_public_name(self):
        """
        Simple getter function to return the publicly accessible name representation. Respects
        user's privacy preferences
        """
        # Private user
        if self.is_private:
            return 'Anonymous'
        # Privacy waived
        else:
            return self.get_alias()
