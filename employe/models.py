from django.db import models

from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

class Employe(AbstractUser):
    phone       = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=True,max_length=15)
    address     = models.TextField(_('Address'),help_text=_('Entrer address'),blank=True,null=True)

class Certificate(models.Model):
    employe     = models.ForeignKey(Employe, on_delete=models.CASCADE)
    certificate = models.FileField(None,upload_to='employe_certificates',null=True,blank=True,default=None)