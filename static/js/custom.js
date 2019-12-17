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
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$('#confirm-delete').on('show.bs.modal', function(e) {	
	$(this).find('.btn-ok').attr('data-href', $(e.relatedTarget).data('href'));	
});

$('.btn-ok').click(function(e){
 	var url = $(this).attr('data-href');
    $.ajax({
        type: "POST",
        url: url,
        beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
        success: function(response) {
        	var message_id = response.message_id
        	$("#tr-row-msg-"+response.message_id).remove()
        	$(".btn-cancel").click();
            if($("#messages-table tbody tr").length < 1){
            	$("#messages-table").hide();
            	$("h1.heading").after("<p>No messages.</p>")
            }
        },
        error: function(data) {
        	console.log(data);
        }
    });
});
