from django.db import models
from django.contrib.auth.models import AbstractUser


class HubUser(AbstractUser):
    """
    Custom User model that adds additional fields for isPrivate and alias information
    """
    pass
    # Add isPrivate field
    is_private = models.BooleanField(default=True)
    # Add alias field
    # Null is allowed as field can be blank and must be unique - prevents constraint exceptions
    alias = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def get_alias(self):
        """Simple getter function to return the user alias. Respects privacy settings"""
        if self.is_private:
            return 'Anonomous'
        else:
            return self.alias
