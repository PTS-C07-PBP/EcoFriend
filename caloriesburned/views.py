from asyncio import constants
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Footprint
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib import messages
from tracker.models import Footprint
from caloriesburned.models import Person
from .forms import userWeight

# Create your views here.
def show_caloriesburned(request):
    if request.user.is_authenticated:
        if Person.objects.filter(user=request.user).exists() == False:
            if request.method == "POST":
                form = userWeight(request.POST)
                if form.is_valid():
                    temp = form.cleaned_data["weight"]
                    t = Person(user=request.user, weight=temp)
                    t.save()
                    response = HttpResponseRedirect(reverse("caloriesburned:show_result"))
                    return response
            else:
                form = userWeight()
            return render(request, 'adding.html', {"form":form})
        else:
            response = HttpResponseRedirect(reverse("caloriesburned:show_result"))
            return response
    else:
        return render(request, 'login.html', {})

def show_result(request):
    tempat = Person.objects.filter(user=request.user)
    berat = tempat[0].weight
    data_mileage = Footprint.objects.all()
    context={
        'berat': tempat[0].weight,
        'list_mileage': data_mileage,
    }
    return render(request, 'showcalories.html', context)

def calories_chart(request):
    date = []
    calories = []

    queryset = Footprint.objects.all()

    for items in queryset:
        date.append(items.date)
        if items.onFoot:
            calories.append(items.mileage*4057.55263)
        else:
            calories.append(items.mileage*0)
        
    return JsonResponse(data={
        'date': date,
        'calories': calories,
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            response = HttpResponseRedirect(reverse("caloriesburned:show_caloriesburned"))
            return response
        else:
            messages.info(request, "Wrong username or password!")
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("caloriesburned:login_user"))
    response.delete_cookie('last_login')
    return response

def show_data(request):
    calories = Footprint.objects.filter(user=request.user)
    return HttpResponse()