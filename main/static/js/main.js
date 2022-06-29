var valid_codes = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]

var context;
function updateContent(content){
    context = content;
}

var responseData = $.ajax({
    url: 'get/user/location/',
    type: 'GET',
    async: false,

    success: function(response){
        console.log('user geo received...', response);
        return updateContent(response);
    },
    error: function(error){
        console.log('error:', error);
    }
    });

console.log(responseData);

let map = L.map('map', {layers: MQ.mapLayer(), maxZoom: 17, minZoom: 0}).setView([context.lat, context.lng], 13);
var dir = MQ.routing.directions();

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    continuousWorld: true,

}).addTo(map);

ImageForm.addEventListener('submit', function(event){

    event.preventDefault();

    var file = $('#ImageForm')[0];
    var formData = new FormData(file);

    var url = new URL('http://127.0.0.1:8000/validate/image/form/');
    var request = new XMLHttpRequest();

    request.open('POST', url, false);
    request.send(formData);

    console.log(request);
    var image_id = JSON.parse(request.response).image_id;
//  there gonna parse image id that method returned....

    console.log('form is valid.....');
    return sendFormImageData(image_id);
});

function sendFormImageData(image_id){

    var request = new XMLHttpRequest();
    var url = new URL("http://127.0.0.1:8000/get/location/geo/data/");
    url.searchParams.append('image_id', image_id);
    request.open('GET', url, false);

    request.send(null);
    console.log(" GET request has been sended....");

    var image_geo_context = JSON.parse(request.response).image_geo_data;
    var root_context = JSON.parse(request.response).root_data;

    console.log(image_geo_context);

    root_time.innerHTML = root_context.total_time;
    root_distance.innerHTML = root_context.total_distance;

//    console.log(String(image_geo_context.lat) + ', ' + String(image_geo_context.lng));
//    console.log('55.754328, 37.610625');
//
//    console.log(    String(context.lat) + '55' + ', ' + String(context.lng) + '55');
//    console.log('43.473107, 11.888702');
//
//    var point_a = String(context.lat) + '55' + ', ' + String(context.lng) + '55';
//    var point_b = String(image_geo_context.lat) + ', ' + String(image_geo_context.lng);

    dir.optimizedRoute({

    locations: [

    '43.473107, 11.888702',
    '55.754328, 37.610625',

        ]
    });

    var CustomRouteLayer = MQ.Routing.RouteLayer.extend({

    createStartMarker:  (location) => {
        var custom_icon;
        var marker;

        custom_icon = L.icon({
            iconUrl: 'https://github.com/ruvictor/map-app-directions/blob/master/img/blue.png?raw=true',
            iconSize: [20, 29],
            iconAnchor: [10, 29],
            popupAnchor: [0, -29],

        });
        marker = L.marker([image_geo_context.lat, image_geo_context.lng], {icon: custom_icon}).addTo(map).bindPopup(context.name).openPopup();
        return marker;
        },
        createEndMarker:  (location) => {
            var custom_icon;
            var marker;

            custom_icon = L.icon({
                iconUrl: 'https://github.com/ruvictor/map-app-directions/blob/master/img/red.png?raw=true',
                iconSize: [20, 29],
                iconAnchor: [10, 29],
                popupAnchor: [0, -29],

            });
            marker = L.marker([context.lat, context.lng], {icon: custom_icon}).addTo(map).bindPopup(context.name).openPopup();
            console.log('marker suppose to work....')
            return marker;
            }
        });

map.addLayer(new CustomRouteLayer({
    directions: dir,
    fitBounds: true
}));

//   L.marker([image_geo_context.lat, image_geo_context.lng]).addTo(map)
//   .bindPopup(String('This is found location'))
//   .openPopup();

}
