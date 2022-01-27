from django.db import models

from import_export.admin import ExportActionMixin

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin,StockMixin
from employe.models import Restaurant

class Meal(TimeStampMixin,MediaMixin,StockMixin,models.Model):
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name          = models.CharField(_('Name'),help_text='Ex:Buger',unique=True, max_length=150, blank=False)
    sale_price    = models.DecimalField(_('Sale Price'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    type          = models.CharField(_('Type'),help_text='Ex:Main', max_length=150, blank=False)

    def __str__(self):
        return 'Name:%s' % (self.name)