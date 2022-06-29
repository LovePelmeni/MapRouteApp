import ipaddress
import json

import requests
from django.test import TestCase
# metro_url = 'https://api.hh.ru/metro/'
# # (station['latitude'], station['longitude'], station['name'])
# # Create your tests here.
# response = requests.get(metro_url, timeout=10)
#
# objects = [(elem['lat'], elem['lng'], elem['name'])
# for elem in json.loads(response.text)
# [0]['lines'][0]['stations'] if json.loads(response.text)[0]['name'] == 'Москва']
#
# cities_lines = [(i['name'], i['lines']) for i in json.loads(
# response.text) if i['name'] == 'Москва']
#
# print(cities_lines)
# ip_address_url = 'http://ipinfo.io/json'

# database = IP2Location.IP2Location(os.path.join("data",
# "IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-"
# "AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-ADDRESSTYPE-CATEGORY-SAMPLE.BIN"))
#
# response_context = {}
# some_url = 'https://api.ip2location.com/v2/?key={YOUR API KEY}&ip=2a00:1370:8125:77c2:8ce8:fb33:1e29:8a8a&format=json&package=WS25&&addon=continent,country,region,city,geotargeting,country_groupings,time_zone_info&lang=zh-cn'
# response = urllib.request.urlopen(ip_address_url, timeout=10)
# response = requests.get(ip_address_url, timeout=10)
# ip = json.loads(response.text)['ip']
# rec = database.get_all("19.5.10.1")
# rec = database.get_all(ip)
# https://api.ip2location.com/v2/?ip=ip_address&key=TJMOW8O72C&package=WS24

# upgraded_ip = ipaddress.IPv6Address('2002::' + ip).compressed
# req_params = {'key': 'TJMOW8O72C', 'ip': ip, 'format': 'json', 'package': 'WS25', 'addon': 'geotargeting'}
# response = requests.get('https://api.ip2location.com/v2/', params={**req_params})
#
# print(response.text)

# loc_data = {
#         'name': 'This Is You',
#         'lat': rec.latitude, 'lan': rec.longitude}
# print(ip)
# def get_location_geo_data(self, name) -> dict:
#     """
#     This method gonna return geo data of the location by specified name argument....
#     :param name: name of the location....
#     :return: Dictionary with name and geo data.... extends with metro location....
#     """
#     response_context = {}
#     from geopy.geocoders import Nominatim
#     loc = Nominatim(user_agent='GetLoc')
#
#     location = loc.geocode(name.replace('_', ' '))
#     loc_data = {
#         'name': name,
#         'lat': location.latitude,
#         'lng': location.longitude,
#     }
#     metro_location = self.get_closest_metro_by_location(loc_data)
#     response_context.update({'location': loc_data, 'metro': metro_location})
#
#     return response_context # place location + metro_location + name_of the search
# ip_address_url = 'http://ipinfo.io/json'
# response = requests.get(ip_address_url, timeout=10)
# ip = json.loads(response.text)['ip']
#
# # ip = tools.get_user_ip_address()
# req_params = {'key': 'TJMOW8O72C', 'ip': ip, 'format': 'json', 'package': 'WS25', 'addon': 'geotargeting'}
# response = requests.get('https://api.ip2location.com/v2/', params={**req_params})
#
# data = json.loads(response.text)
            # response = urllib.request.urlopen(ip_address_url, timeout=10)
            # ip = json.loads(response.text)['ip']
            # rec = database.get_all(ip)
# loc_data = {
# 'name': 'This Is You',
# 'lat': data['latitude'], 'lng': data['longitude'],
# 'region_name': data['region_name'].replace("'", "")
# }
#
# print(loc_data)

# if 'search_params' in request.COOKIES:
#     #saving history data to file from the cookies.
#
#     # with open(request.COOKIES['search_params'], mode='w') as hist_file:
#     #     hist_file.write(name)
#     #     logger.debug('search param has been written to file....')
#     #
#     # context['history'] = hist_file.readlines()
#     # hist_file.close()
# import io
#
# print(io.BytesIO())

# def get_metro_info_list(self):
#     """
#     Sending request to API and gets list of metro data....
#     :return: List of corteges with 3 elements: 'coords' and name of metro station...
#     """
#     if not 'stations_list' in stations_db.keys():
#
#         stations_db['stations_list'] = []
#         logger.debug('applying stations data to database....')
#
#         return tools.apply_all_stations_to_db()
#
#     logger.debug('Getting stations data from shelve db.....')
#     return stations_db['stations_list']

# def get_closest_metro_by_location(self) -> dict:
#     """
#     Comparing coords of the stations and finding most closest....
#     :return: coordinates + name of the metro, that is most closest to this place....
#     """
#     location_data = self.get_user_geo_data_by_ip()
#
#     metro_data = {}
#
#     station = min(self.get_metro_info_list(),
#     key=lambda coord: (round(coord[0], 2) - round(location_data['lat'], 2), #finding minimal lng and lat from
#     # the whole query and returns cortege
#     round(coord[1], 2) - round(location_data['lng'], 2)))
#     metro_data.update({'lat': round(station[0], 2), 'lng': round(station[1], 2), 'name': station[3]})
#
#     return {'location': location_data, 'metro': metro_data}


# class CheckLocationValidView(main_geo_api.GeoSearchMixin, View):
#     """This function checks for restrictions depends on the user location"""
#
#     def get(self, request, **options):
#         list_of_valid_places = ['Moscowskaya Oblast', 'Moscow']
#
#         from django.http import HttpResponseForbidden
#         location = self.get_user_geo_data_by_ip()
#
#         if location['region_name'] in list_of_valid_places:
#             request.set_signed_cookie('is_restricted', True).set_expiry(0)
#
#         if not 'is_restricted' in request.COOKIES:
#             return HttpResponse(200)
#
#         return HttpResponseForbidden()

# def apply_all_stations_to_db():
#     """Getting all stations info from the url and sending signal to apply it to shelve db...."""
#     all_stations = []
#     try:
#         import requests
#         response = requests.get(metro_url, timeout=10)
#         import json
#         data = json.loads(response.text)
#
#         for elem in range(len(data) + 1):
#             stations = [(station['lat'], station['lng'], station['name']) for station in
#             data[elem]['lines'][elem]['stations']]
#
#             all_stations.append(stations)
#
#     except TimeoutError as tm_err:
#         logger.error('server has been waited for so long for response %s' % tm_err)
#
#     return to_db.send(sender=apply_all_stations_to_db, list_of_stations=all_stations)
# import json
# ACCESS_KEY = 'TJMOW8O72C'
# ip_address_url = 'http://ipinfo.io/json'
# response = requests.get(ip_address_url, timeout=10)
# ip = json.loads(response.text)['ip']
#
# req_params = {'key': ACCESS_KEY, 'ip': ip, 'format': 'json', 'package': 'WS25', 'addon': 'geotargeting'}
# response = requests.get('https://api.ip2location.com/v2/', params={**req_params}, timeout=15)
#
# data = json.loads(response.text)
# loc_data = {
#             'name': 'This Is You', 'lat': data['latitude'],
#             'lng': data['longitude']}
#
# print(loc_data)


# ip_address_url = 'http://ipinfo.io/json'
# response = requests.get(ip_address_url, timeout=10)
# ip_address = json.loads(response.text)['ip']
#
# url = 'https://geolocation-db.com/jsonp/' + str(ip_address)
# response = requests.get(url, timeout=10)
# result = response.content.decode()
#
# result = result.split("(")[1].strip(")")
# # Convert this data into a dictionary
# result = json.loads(result)
# print(result)


# with open(uploaded_image_url, 'rb') as _:
#     # with open(uploaded_image_url, mode='rb') as _ :
#     exif_file = exif.Image(_)
#     logger.debug('start parsing meta data from image...')
#
#     print(uploaded_image_url)
#     return self.get_image_gps(exif_file)


# import exifread
# metadata = {}
# exif_tags = exifread.process_file(img)
# print(exif_tags, 'exif_tags')
#
# # if 'GPS' in [elem.upper() for elem in exif_tags.keys()]:
# metadata['longitude'] = exif_tags.get('GPS GPSLongitude')
# metadata['latitude'] = exif_tags['GPS GPSLatitude']
#
# print(metadata)
# return metadata

#
# print(dir(img))
# print(img.get_all())
#
# if img.has_exif:
#     print(img.gps_latitude,
#           img.gps_longitude)
#
#     lng = img.get('gps_longitude')[0]
#     lat = img.get('gps_latitude')[0]
#
#     data = {'lng': lng, 'lat': lat}


# def is_metadata_in_image(self, link):
#     try:
#         with open(link, mode='rb') as some_file:
#             exif_file = exif.Image(some_file)
#
#             if exif_file.has_exif and ('gps_latitude',
#             'gps_longitude') in exif_file.get_all().keys():
#                 return True
#
#             return False
#     except OSError:
#         return False
# dictin = {'elem': 'value', 'some_new_elem': 'some_new_value'}
# print({**{elem: value for elem, value in dictin.items()}})
from PIL import Image
# with open('C:\\Users\dell\Desktop\\random_image.jpg', mode='rb') as upl_file:
#     file = Image(upl_file)
#     if file.has_exif:
#         print(file.get_all())
#     else:
#         print('image has no exif...')
# image = Image.open('https://www.pic2map.com/photos/tkbltq.jpg')
# print(image.info)
# import exif
# with open('https://www.pic2map.com/photos/thumbs/iashk.jpg', mode='rb') as file:
#     exif = exif.Image(file)
#     print(exif.has_exif, exif.get_all())

# with open(uploaded_image_url, mode='rb') as upl_file:
#
#     file = exif.Image(upl_file)
#     if file.has_exif:
#         print(file.get_all())
#         logger.debug('info found....')
#
#         return {**{elem: value for elem, value
#     in file.get_all().items() if elem in geo_attrs}}

# def start_root(request):
#     from . import tools
#     tools.share_user_geo_data(request)
#     return HttpResponse(status=200)

# class ResumeUploadView(View):
#
#     def get(self, request):
#         if not 'Range' in request.HEADERS:
#             return HttpResponseNotFound()
#
#         logger.debug('continue uploading...')
#         return resume_file_uploading(request)
#
# def get_full_image_link(obj):
#     from django.conf import settings
#     return settings.MEDIA_ROOT + obj.image.name
#
# def resume_file_uploading(request):
#     from .models import ImageModel
#
#     header = request.headers.get('Range', None)
#     file_resume_index = header.split('0')[1]
#
#     image_id = request.GET.get('image_id')
#     image_link = get_full_image_link(ImageModel.objects.get(
#     id=image_id))
#
#     with open(image_link, mode='rb') as some_file:
#         some_file.seek(file_resume_index)
#         content = some_file.read(file_resume_index)
#
#     return django.http.StreamingHttpResponse(streaming_content=content,
#     content_type='image/jpg')
#
#
            # for elem, value in {elem: value for elem, value in exif_data.items() if not isinstance(value, bytes)}.items():
            #     if elem in required_params:
            #         filtered_data[elem] = exif_data[elem].decode()

# image = Image.open(uploaded_image_url)
        # image.verify()
        # try:
        #     exif = image._getexif()
        #     print(exif, image.info, image.getexif())
        #     gps_data = {elem: value for elem, value in
        #     tools.get_gps_tags(exif) if elem in geo_attrs}

        #     return gps_data

        # except ValueError:
        #     logger.debug('None gps data was found in this file')
        #     return None 

coords = [(56.3, 47.21), (45, 76)]
coords_list = [str(elem).strip('()').replace(' ', '') for elem in coords]
print(coords_list[0] + ';' + coords_list[1])
