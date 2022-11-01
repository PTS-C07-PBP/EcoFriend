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
            }  
        }
    )
}

$(`#submit-button`).attr('onclick', `addMotivation()`);

const changeButton = document.getElementById('change-button');

function getMotivation() {
    $.get(
        '../get_motive/',
        (res) => {
            console.log(res)
            let long = res.length;
            const indeks = Math.floor(Math.random() * long);
            $('#motive-container').empty();
            $('#motive-container').append(
                `
                <div class="flex-zero">
                    <h5>${res[indeks].fields.sentences}</h5>
                </div>
                `
            )
        }
    )
}
$(`#change-button`).attr('onclick', `getMotivation()`);
