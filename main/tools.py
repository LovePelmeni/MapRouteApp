from typing import List

import requests
from django import dispatch
import logging

from django.core.exceptions import ValidationError

metro_url = 'https://api.hh.ru/metro/'
to_db = dispatch.Signal()
ACCESS_KEY = 'TJMOW8O72C' # need to receive access token at first......

logger = logging.getLogger(__name__)

def get_user_ip_address():
    import json

    ip_address_url = 'http://ipinfo.io/json'
    response = requests.get(ip_address_url, timeout=10)
    ip = json.loads(response.text)['ip']

    return ip

def get_full_image_url(image_id: int):
    from django.conf import settings
    from .models import ImageModel

    some_image = ImageModel.objects.get(id=image_id)
    full_url = settings.MEDIA_ROOT + some_image.image.name

    return full_url

def get_total_time_by_car(speed, distance): # speed should be in km per hour 
    return '%s hours' % round(distance / speed, 1)

def get_total_route_kwargs(coords: List[tuple]):
    from geopy.distance import distance
    total_distance = round(distance(coords[0], coords[1]).km, 1)
    data = {
        'total_distance': '%s km' % total_distance,
        'total_time': get_total_time_by_car(speed=100, distance=total_distance)
    }
    return data

def validate_image(image):
    import os
    valid_extensions = ['.jpg', '.png', '.jpeg']

    image_name = image.name
    file, extension = os.path.splitext(image_name)
    if extension.lower() in valid_extensions:
        return image

    raise ValidationError('image is not valid...')

def handle_coords_empty_exception(response_data):
    from django.http import HttpResponse
    import json

    response = HttpResponse()
    response.status_code = response_data['status_code']

    response.data = json.dumps(response_data['error_context'])
    response.content_type = 'application/json'

    return response

class ImageAlreadyExistsError(Exception):
    def __init__(self, message):
        self.message = message

    def __call__(self, *args, **kwargs):
        return self.message

def check_file_identity(files, to):
    import filecmp
    result_list = []

    for elem in files:
        result_list.append(filecmp.cmp(elem, to))

    if not all(result_list):
        raise ImageAlreadyExistsError(message='File Already Exists')

