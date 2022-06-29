from django.contrib import admin

# Register your models here.
from .models import ImageModel


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']
    fields = ['image']

admin.site.register(ImageModel, ImageAdmin)



