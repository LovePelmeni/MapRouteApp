var geo = null;

function process_geo_data(content){
    geo = content;
//    return initMap(geo);
}

var source_url = new URL('http://127.0.0.1:8000/map/events/');
source_url.searchParams.append('channel', 'map_channel');

var source = new EventSource(source_url);

source.onopen = function(){
    console.log('source has been opened....');
}

source.addEventListener('message', function(event){

    var data = JSON.parse(event.data);
    console.log('message has been received....', data);
    var prepared_obj = {

        'name': responseData.geo_data.location.name,
        'lat': responseData.geo_data.location.lat,
        'lng': responseData.geo_data.location.lng,

        }
        console.log(prepared_obj);
        return process_geo_data(prepared_obj);
});

source.onerror = function(error){

    source.close();
    console.log('error has occurred', error);
}
