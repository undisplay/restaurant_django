from django.db import models

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class MediaMixin(models.Model):
    image = models.ImageField(upload_to ='products/images/',null=True,blank=True)

    class Meta:
        abstract = True