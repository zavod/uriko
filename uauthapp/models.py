from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _

# Create your models here.
USER_ROLES = (
    ('client', _('Client')),
    ('admin', _('Admin')),
    ('expert', _('Expert')),
    ('consultant', _('Consultant')),
)

class CabinetUser(User):
    role = models.CharField(_('Role'), max_length=250, choices=USER_ROLES, default=_('Client'))

    objects = UserManager()

    @staticmethod
    def create_for_exist(user, role='client'):
        newuser = CabinetUser(user_ptr=user, username=user.name,
                              password=user.password, email=user.email,
                              first_name=user.first_name, last_name=user.last_name,
                              is_active=user.is_active, is_staff=user.is_staff,
                              last_login=user.last_login, date_joined=user.date_joined,
                              role=role, is_superuser=user.is_superuser)
        newuser.save()
        return newuser

class Document(models.Model):
    pass
    