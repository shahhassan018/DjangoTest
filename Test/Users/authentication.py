from django.contrib.auth.models import User;
from django.core.exceptions import ValidationError

#Email AuthBackend purpose
class EmailAuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            raise ValidationError("Invalid Credentials")


    def get_user(self, user_id):
        try:
         return User.objects.get(pk=user_id)
        except User.DoesNotExist:
         return None
