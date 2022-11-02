
function posting(e) {
    e.preventDefault()
    const title = $("#title").val()
    const rating = $("#rating").val()
    const description = $("#description").val()

    const data = {
        title: title,
        rating: rating,
        description: description,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    }

    $.ajax({
        type: 'POST',
        url: "/review/addreview/",
        data: data,
        dataType: 'json',
        // success: add_review()
        success: function(data){
            console.log(data)
            $('#main-div').append(`
                <div class="card col-sm-4 mb-1 mt-4 mx-auto" style="width: 18rem;">
                <div class="card-body">
                    <h4 class="card-title text-center fw-semibold">${data[0].title}</h4>
                    <ul class="list-group list-group-flush">
                    <li class="list-group-item text-secondary">${data[0].user__username}</li>
                    <li class="list-group-item text-secondary">${data[0].date}</li>
                    <li class="list-group-item text-secondary">${data[0].rating}</li>
                    <li class="list-group-item">${data[0].description}</li>
                    </ul>
                </div>
                </div>
            `
            );   
        }
    })
   
    $('#title').val('')
    $('#rating').val('')
    $('#description').val('')

}

function fetchData() {
    $.get("/review/json", update)
}

$(document).ready(() => {
    $("#create-button").click(posting)
    add_review()
})

function add_review() {
    $.get("/review/json", function (data) {
        $('#main-div').html("");
        $.each(data, function (index, review) {
             $('#main-div').append(`
                <div class="card col-sm-4 mb-1 mt-4 mx-auto" style="width: 18rem;">
                <div class="card-body">
                    <h4 class="card-title text-center fw-semibold">${review.title}</h4>
                    <ul class="list-group list-group-flush">
                    <li class="list-group-item text-secondary">Username: ${review.user__username}</li>
                    <li class="list-group-item text-secondary">Date: ${review.date}</li>
                    <li class="list-group-item text-secondary">Rating: ${review.rating} of 5</li>
                    <li class="list-group-item">${review.description}</li>
                    </ul>
                </div>
                </div>
            `
            );       

        })
    }
    )
}
