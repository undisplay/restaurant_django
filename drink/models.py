from django.db import models

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin

class Drink(TimeStampMixin,MediaMixin,models.Model):
    class Types(models.TextChoices):
        SOFT    = 'SOFT', _("SOFT")
        BEER    = 'BEER', _("BEER")
        LIQUOR  = 'LIQUOR', _("LIQUOR")
    
    name          = models.CharField(_('Name'),help_text='Ex:Coca',unique=True, max_length=150, blank=False)
    price         = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    sale_price    = models.DecimalField(_('Sale Price'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    sale_price_ml = models.DecimalField(_('Sale Price(ml)'),help_text=_('Ex: 5'),max_length=255,max_digits=11,decimal_places=2,blank=True,null=True)
    type          = models.CharField(_('Type'),help_text='Ex:Soft drink',max_length=25,choices=Types.choices,default=Types.SOFT,blank=False)
    
    def __str__(self):
        return 'Name:%s Type:%s' % (self.name,self.type)
