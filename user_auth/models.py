from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Custom User Model for future enhancements
class CustomUser(AbstractUser):
    """
    Extends Django's default User model
    Can add additional fields in the future such as:
    - phone_number = models.CharField(max_length=15, blank=True)
    - address = models.TextField(blank=True)
    - profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    """
    # Resolve conflict with the default User model
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',
        related_query_name='customuser'
    )
