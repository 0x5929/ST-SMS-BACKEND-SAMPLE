from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        # if we are authenticating and NOT using username, then extract email!
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return None

        # at this point, username is either username or email
        # next we need to fetch users using either username or email (case insensitive)
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # if the user does not exist, do not create new user
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
