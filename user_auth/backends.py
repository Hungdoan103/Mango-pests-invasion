from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication using email or username
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Find user by email or username
            user = UserModel.objects.filter(
                Q(username__iexact=username) | 
                Q(email__iexact=username)
            ).first()
            
            if user and user.check_password(password):
                return user
            return None
        except UserModel.DoesNotExist:
            return None
