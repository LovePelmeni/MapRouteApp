from django import forms
from .models import ImageModel
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Your Image', required=True)

    class Meta:
        model = ImageModel
        fields = ['image']


