from django import http
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from tracker.models import Footprint
from .models import Comment
from django.contrib.auth import get_user_model
from django.core import serializers
from .forms import CommentForm


# Create your views here.


def show_leaderboard(request):
    if request.user.is_authenticated:
        form = CommentForm()

        data = []
        User = get_user_model()
        comment = Comment.objects.all()
        user_list = User.objects.all()
        for user1 in user_list:
            tracker = Footprint.objects.filter(user=user1.pk)
            sum_mileage = 0
            sum_carbon = 0
            for fp in tracker:
                sum_mileage += fp.mileage
                sum_carbon += fp.carbon
            if sum_mileage:
                data.append([user1, sum_carbon/sum_mileage, sum_mileage, sum_carbon])
        data.sort(key=lambda x: x[1])
        context = {
            'list': data,
            'form': form,
            'comments': comment
        }
        return render(request, 'leaderboard.html', context)
    form = CommentForm()
    return render(request, 'denied.html', {'form': form})

@login_required
def add_comment(request):
    if request.method == 'POST':
        newComment = Comment(
           user=request.user,
            comment=request.POST.get('comment')
        )
        newComment.save()
        return JsonResponse({
            'user': newComment.user.username,
            'comment': newComment.comment
        })
    return render(request, 'leaderboard.html', {})

def show_comment(request):
    data = Comment.objects.all()
    print(data)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize('json', data))

def show_json_footprint(request):
    data = Footprint.objects.all()
    return HttpResponse(serializers.serialize('json', data))

def show_json_user_detail(request):
    data = []
    for items in Footprint.objects.filter(user=request.user):
        data.append({
            "Rank" : str(items.to_order),
            "Name": str(items.user),
            "Mileage": int(items.mileage),
            "Footprint": str(items.carbon),
        })

    return JsonResponse(data, safe=False)
