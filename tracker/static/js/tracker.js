function refreshHistory() {
  $.getJSON("/tracker/get_data", function (data) {
    // ITERATING THROUGH OBJECTS
    $.each(data, function (key, value) {
      var history = '';

      history += '<div class="col">'
      history += '<div class="card border-success mb-3" style="max-width: 18rem" id="card">'
      history += '<div class="card-header" id="header">'
      history += value.fields.datetime_show + '</div>'
      history += '<div class="card-body text-success" id="body">'
      history += '<p class="card-text" id="carbon">'
      history += 'You traveled for ' + value.fields.mileage + ' km and create as much as ' + value.fields.carbon + ' kg of carbon footprint</p>'
      history += '</div>'
      history += '</div>'
      history += '</div>'
      history += '</div>'

      $("#deck").append(history);
    });
  });
}

function addData() {
  $.ajax({
    method:'POST',
    url:"/tracker/create_data",
    data:{
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      mileage:$('#mileage').val(),
      type:$(".btn-check:checked").val(),
      action: 'post'
    },
    success:function(json){
      $('#mileage').val(""),
      refreshHistory();
    },
  });
}

$(document).ready(function() {
  refreshHistory()
})