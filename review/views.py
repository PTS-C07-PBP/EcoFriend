import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from review.forms import NewForm
from review.models import Review
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
from .models import Review
@login_required(login_url='/review/login/')
def create_review(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            review = Review(
                user=request.user,
                title=form.cleaned_data["title"],
                rating=form.cleaned_data["rating"],
                description=form.cleaned_data["description"],
            )
            review.save()
            return redirect("review:show_review_ajax")

    form = NewForm()
    context = {"form": form}
    return render(request, "review_ajax.html", context)


def show_review_ajax(request):
    data = Review.objects.all()
    context = {
        'review_list': data,
    } 
    return render(request, "review_ajax.html", context)

def show_json(request):
    
    data = Review.objects.values('user__username', 'title', 'description', 'rating', 'user', 'date')
    return HttpResponse(json.dumps(list(data), indent=4, sort_keys=True, default=str), content_type="application/json")

def add_review(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        rating= request.POST.get('rating')
        description = request.POST.get('description')
        new_review = Review(
            date=str(datetime.date.today()),
            title=title, 
            rating=rating,
            description=description,
            user=request.user,
        )
        new_review.save()

        review = Review.objects.filter(pk=new_review.pk).values('user__username', 'title', 'description', 'rating', 'user', 'date')
        return HttpResponse(json.dumps(list(review), indent=4, sort_keys=True, default=str), content_type="application/json")

        # return HttpResponse(serializers.serialize("json", review), content_type="application/json")
 