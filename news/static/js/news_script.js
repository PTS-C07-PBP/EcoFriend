// Menggabungkan data article dengan sintaks HTML
function makeArticle(article) {
    if (article.fields.admin_created) {
        var html = "<div id='"+article.pk+"' class='col'><div class='card border border-success'><div class='card-body'><h5 class='card-title'><a href="+article.fields.link+">"+article.fields.title+"</a></h5>"
            html += "<p class='card-text'><small class='text-muted'>"+article.fields.date+"</small></p><p class='card-text'><small class='text-muted'>"+article.fields.region+"</small></p><p class='card-text'>"+article.fields.description+"</p>"
        if (article.fields.user == $('#current_user').text()) {
            html +="<button class='btn' onclick='deleteArticle("+article.pk+");'>Delete</button></td></tr></div></div></div>"
        }
    } else {
        var html = "<div id='"+article.pk+"' class='col'><div class='card border border-success'><img src="+article.fields.image+"class='card-img-top' width='200px'><div class='card-body'><h5 class='card-title'><a href="+article.fields.link+">"+article.fields.title+"</a></h5>"
        html += "<p class='card-text'><small class='text-muted'>"+article.fields.date+"</small></p><p class='card-text'><small class='text-muted'>"+article.fields.region+"</small></p><p class='card-text'>"+article.fields.description+"</p></div></div></div>"
    }
    return html;
}

// Menambah 10 article dan pagination
function add_articles(page_num) {
    $.get("/news/articles/", {'region':$('#id_filter_region').val(), 'page_num':page_num}, function(data) {
        $('#articles').html('');
        $.each(data[0], function(index, article) {
            $('#articles').append(makeArticle(article));
        });
        $('#pagination').html('');
        for (var page_num = 1; page_num <= data[1]; page_num++) {
            $('#pagination').append("<button type='button' class='btn' onclick='paginate("+page_num+");'>"+page_num+"</button>");
        }
    });
}
    
// Get article saat load
$(document).ready(function(){
    $.get("/news/init/", function(data) {
        $.each(data[0], function(index, article) {
            $('#articles').append(makeArticle(article));
        });
        $('#pagination').html('');
        for (var page_num = 1; page_num <= data[1]; page_num++) {
            $('#pagination').append("<button type='button' class='btn' onclick='paginate("+page_num+");'>"+page_num+"</button>");
        }
    });
});

// Filter article sesuai region
$('#id_filter_region').change(function() {
    add_articles(1);
});

// Fungsi saat menekan pagination
function paginate(page_num) {
    add_articles(page_num);
}

// Menambah article baru khusus admin
$(".btn-add-article").click(function(e) {
    e.preventDefault();
    $.post("/news/add/", {title: $('#id_title').val(), region: $('#id_region').val(), description: $('#id_description').val(), csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()}, function(data) {
        $("#num_created_articles").html(data);
        if (parseInt(data) <= 1) {
            $("#article_articles").html(' article.');
        } else {
            $("#article_articles").html(' articles.');
        }
        add_articles(1);
    });
});

// Menghapus article yang dibuat admin
function deleteArticle(pk) {
    $.ajax({
        url: "/news/delete/"+pk,
        method: "DELETE",
        dataType: "json",
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name=csrfmiddlewaretoken]').val());
        },
        success: function(data) {
            $("#num_created_articles").html(data);
            if (parseInt(data) <= 1) {
                $("#article_articles").html(' article.');
            } else {
                $("#article_articles").html(' articles.');
            }
            add_articles(1);
        }
    });
}