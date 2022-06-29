from django.core.files.storage import FileSystemStorage
from django.db import models


storage = FileSystemStorage()

class ImageModel(models.Model):
    objects = models.Manager()

    name = models.CharField(verbose_name='Name', null=True, max_length=100)
    image = models.ImageField(verbose_name='Image', storage=storage, null=False)



