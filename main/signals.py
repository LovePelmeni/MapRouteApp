import shelve
from django.dispatch import receiver
from .tools import to_db

@receiver(to_db)
def append_list_to_db(sender, list_of_stations, **kwargs):
    with shelve.open('metros') as stations_db:
        stations_db['stations_list'].append(list_of_stations)

    return list_of_stations


