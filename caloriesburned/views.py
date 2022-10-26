from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Footprint
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def show_caloriesburned(request):
    context = {
        'nama': request.user,
        }
    if request.user.is_authenticated :
        return render(request, 'submit.html', context)
    else:
        return render(request, 'login.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            response = HttpResponseRedirect(reverse("caloriesburned:submit.html"))
            return response
        else:
            messages.info(request, "Wrong username or password!")
    context = {}
    return render(request, 'login.html', context)
