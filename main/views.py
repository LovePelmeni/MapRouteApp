from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
import django.core.exceptions

from .models import ImageModel
from . import forms, main_geo_api
from django.http import JsonResponse
# Create your views here.

from django.views import View
import logging

logger = logging.getLogger(__name__)

def main_page(request):
    context = {}
    template_name = 'main/index.html'

    context['title'] = 'Main Page'
    context['form'] = forms.ImageForm()

    return render(request, template_name, context=context)

@csrf_exempt
def validate_form_image(request):
    from django.db import transaction
    from django.http import HttpResponseForbidden, HttpResponseBadRequest
    from . import tools
    context = {}

    if not request.is_ajax:
        return HttpResponseForbidden()
    try:
        with transaction.atomic():
            image = request.FILES.get('image')
            tools.validate_image(image)

            new_image, created = ImageModel.objects.get_or_create(image=image,
            name=image.name, defaults={'image': image, 'name': image.name})

            context.update({'image_id': new_image.id})

    except django.core.exceptions.ValidationError as v_err:
        logger.debug('image form is not valid.... %s' % v_err.message)
        return HttpResponseBadRequest

    return JsonResponse(data=context, status=200)

def get_entire_location(request):
    logger.debug('start searching...')

    return main_geo_api.GeoSearchMixin(
    ).prepare_all_geo_data(request)

class UserGeoView(main_geo_api.GeoSearchMixin, View):

    def get(self, request):
        geo_data = self.get_user_geo_data_by_ip()
        return JsonResponse(geo_data)

