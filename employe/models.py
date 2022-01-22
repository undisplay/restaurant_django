from django.db import models

from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin

class Employe(TimeStampMixin,MediaMixin,AbstractUser):
    phone       = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=True,max_length=15)
    address     = models.TextField(_('Address'),help_text=_('Entrer address'),blank=True,null=True)

    def __str__(self):
        return 'Firstname:%s Lastname:%s' % (self.first_name,self.last_name)
