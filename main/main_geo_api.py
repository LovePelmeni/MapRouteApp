from django.http import JsonResponse
from . import tools
import logging

ip_address_url = 'http://ipinfo.io/json'
valid_codes = [code for code in range(200, 210)]

logger = logging.getLogger(__name__)

class GeoSearchMixin(object):
    """
    This is Mixin contains necessary methods to find
    geo data of user location and some extra stuff.....
    """
    def get_geo_data_from_image(self, request):
        import exifread

        image_id = request.GET.get('image_id')
        uploaded_image_url = tools.get_full_image_url(image_id)
        gps_data = {'image_url': uploaded_image_url}

        with open(uploaded_image_url, mode='rb') as file:
            exif_data = exifread.process_file(file)

            gps_coords = [round(elem, 6) for elem in exifread.utils.get_gps_coords(exif_data)]
            gps_data.update({'lat': gps_coords[0], 'lng': gps_coords[1]})

        file.close()
        return gps_data 

    def get_user_geo_data_by_ip(self):
        import json, requests

        try:
            ip = tools.get_user_ip_address()
            url = 'https://geolocation-db.com/jsonp/' + str(ip)

            response = requests.get(url, timeout=20)
            result = response.content.decode().split("(")[1].strip(")")
            # Convert this data into a dictionary
            data = json.loads(result)
            loc_data = {
                'name': 'You are here', 'lat': data['latitude'],
                'lng': data['longitude']}

            return loc_data

        except requests.exceptions.Timeout as tm_err:
            logger.error('server has been waiting for so long %s' % tm_err)

        except requests.exceptions.ConnectionError as conn_err:
            logger.error('some error with connection....', conn_err.response)

    def prepare_all_geo_data(self, request):

        image_geo = self.get_geo_data_from_image(request)
        user_geo = self.get_user_geo_data_by_ip()

        if not image_geo.items():
            context = {'error_context': {'message': 'This Photo does not match :('},
            'status_code': 400}
            return tools.handle_coords_empty_exception(context)

        root_kwargs = tools.get_total_route_kwargs([(image_geo['lat'],
        image_geo['lng']),
        (user_geo['lat'], user_geo['lng'])])

        geo_data = {
            'image_geo_data': image_geo,
            'root_data': root_kwargs,
        }
        return JsonResponse(geo_data)

