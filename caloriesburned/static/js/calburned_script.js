$(function(){
    var $caloriesChart = $("#calories-chart");
    $.ajax({
        url: $caloriesChart.data("url"),
        success: function(data){

            var ctx = $caloriesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.date,
                    datasets: [{
                        label: 'Calories',
                        backgroundColor: 'lightgreen',
                        data: data.calories,
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Calories Burned Chart'
                    }
                    
                }
            });

        }
    });
});

const submitButton = document.getElementById('submit-button');

function addMotivation() {
    let form = $('#add-motive-form')
    $.post(
        {
            url: '../add_motive/',
            data : form.serialize(),
            success: (response) => {
                confirm("Motivation saved!");
                $('input[name=motive]').val("");
                getLastSubmit();
            }  
        }
    )
}

function getLastSubmit() {
    $.get(
        '../get_last_submit/',
        (res) => {
            $('#last-login-container').empty();
            $('#last-login-container').append(
                `
                <div class="flex-two">
                    <h6>Last submit motivation: ${res.last_submit}</h6>   
                </div>
                `
            )
        }
    )
}

$(`#submit-button`).attr('onclick', `addMotivation()`);

const changeButton = document.getElementById('change-button');

function getMotivation() {
    $.get(
        '../get_motive/',
        (res) => {
            let long = res.length;
            const indeks = Math.floor(Math.random() * long);
            $('#motive-container').empty();
            $('#motive-container').append(
                `
                <div class="flex-two">
                    <h5>${res[indeks].fields.sentences}</h5>
                </div>
                `
            )
        }
    )
}
$(`#change-button`).attr('onclick', `getMotivation()`);
