from django.urls import path
from . import views, tools

urlpatterns = [

    path('', views.main_page, name='home'),
    path('get/location/geo/data/', views.get_entire_location, name='geo_data'),
    path('validate/image/form/', views.validate_form_image, name='validate_image_form'),
    path('get/user/location/', views.UserGeoView.as_view(), name='user_geo_data'),

]
