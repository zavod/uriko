from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from django.contrib.auth.models import User

class CabinetUserAuth(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class.objects.get(username=username)
            if user.chech_password(password)
                return user
        except self.user_class.DoesNotExist:
            try:
                olduser = User.objects.get(username=username)
                if olduser.check_password(password)
                    user = olduser.user_class.create_for_exist(olduser)
                    return user
            except User.DoesNotExist:
                pass
            return None
    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None

    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CABINET_USER_MODEL.split('.',2))
            if not self._user_class:
                raise ImproperlyConfigured('please set CABINET_USER_MODEL in settings.py')
        return self._user_class
