from django.shortcuts import render
from tracker.models import Footprint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages



# Create your views here.

def show_leaderboard(request):
    if request.user.is_authenticated:
        data = Footprint.objects.all().order_by('-to_order').reverse
        context = {
            'list': data,
        }
        return render(request, 'leaderboard.html', context)
    else:
        return render(request, 'denied.html', {})