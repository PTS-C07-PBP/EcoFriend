function refreshHistory() {
  $.getJSON("/tracker/get_data", function (data) {
    var history = '';

    $.each(data, function (key, value) {

      history += '<div class="card" id="card">'
      history += '<div class="card-header" id="header">'
      history += value.fields.datetime_show + '</div>'
      history += '<div class="card-body" id="body">'
      history += '<p class="card-text" id="text">'
      history += 'You traveled for ' + value.fields.mileage + ' km and create as much as ' + value.fields.carbon + ' g of carbon footprint</p>'
      history += '</div>'
      history += '</div>'

    });
    document.getElementById("deck").innerHTML = history;
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