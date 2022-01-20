from django.db import models
from django.utils.translation import gettext_lazy as _

class StockMixin(models.Model):
    quantity_available = models.IntegerField(_('Quantity available'),help_text=_('Ex: 1'),blank=False,default=1)

    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class MediaMixin(models.Model):
    image = models.ImageField(upload_to ='products/images/',null=True,blank=True)

    class Meta:
        abstract = True