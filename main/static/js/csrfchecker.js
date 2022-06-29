//(function() {
//     var send = XMLHttpRequest.prototype.send,
////          token = document.getElementById('meta')['x-csrf-token'].content;
//     token = $.getCookie('csrftoken');
//     XMLHttpRequest.prototype.send = function(data) {
//          this.setRequestHeader('X-CSRF-Token', token);
//          return send.apply(this, arguments);
//     };
//}());

var csrftoken = $.getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


