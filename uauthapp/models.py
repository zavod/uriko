from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _

# Create your models here.
USER_ROLES = (
    ('client', _('Client')),
    ('expert', _('Expert')),
    ('consultant', _('Consultant')),
)

class CabinetUser(User):
    role = models.CharField(_('Role'), max_length=250, choices=USER_ROLES, default=_('Client'))
    name =  models.CharField(_('Name'), max_length=250)

class Document(models.Model):
    pass
    