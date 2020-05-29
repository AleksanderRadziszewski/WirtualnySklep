function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function add_product(event){
    var csrftoken = getCookie('csrftoken');
    $.post({
            url: "/add_product_to_cart/",
            data: {
                csrfmiddlewaretoken: csrftoken,
                id_product:this.dataset.id
            },
            function(data, status){
                alert(status);
            }
        });

}

$(document).ready(function () {
    $("#order").click(add_product);

});

function increase_quantity() {
    var csrftoken = getCookie('csrftoken');
    $.post({
            url: "/changequantity/",
            data: {
                csrfmiddlewaretoken: csrftoken,
                id_product: this.dataset.id,
            },
            function(data, status){
                alert(status);
            }
        });

}

$(document).ready(function (event) {
    event.preventDefault()
    $("#increase").click(increase_quantity);

});

