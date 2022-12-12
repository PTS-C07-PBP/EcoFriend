function refreshHistory() {
  $.getJSON("/user/show_notes", function (data) {
    var history = '';

    $.each(data, function (key, value) {

      history += '<div class="card" id="card">'
      history += '<div class="card-body" id="body">'
      history += '<p class="card-text" id="text">'
      history += value.fields.notes
      history += '</div>'
      history += '</div>'

    });
    document.getElementById("note-deck").innerHTML = history;
  });
}

function addNotes() {
  $.ajax({
    method:'POST',
    url:"/user/add_notes",
    data:{
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      notes:$('#my-note').val(),
      action: 'post'
    },
    success:function(json){
      $('#my-note').val(""),
      refreshHistory();
    },
  });
}

$(document).ready(function() {
  refreshHistory()
})
  