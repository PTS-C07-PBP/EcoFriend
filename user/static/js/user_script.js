
function addNotes() {
    var html = "<div id='"+article.pk+"' class='col'><div class='card border border-success'><div class='card-body'><h5 class='card-title'><a href="+article.fields.link+">"+article.fields.title+"</a></h5>"
    html += "<p class='card-text'><small class='text-muted'>"+article.fields.date+"</small></p><p class='card-text'><small class='text-muted'>"+article.fields.region+"</small></p><p class='card-text'>"+article.fields.description+"</p>"
}