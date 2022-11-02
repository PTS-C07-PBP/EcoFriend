from asyncio import constants
import datetime
import json
import random
from re import M
from time import timezone
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Footprint
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib import messages
from tracker.models import Footprint
from caloriesburned.models import Person, Motive
from .forms import userWeight, addMotive
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect

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
        return render(request, 'loginalert.html', {})

def show_result(request):
    tempat = Person.objects.filter(user=request.user)
    data_mileage = Footprint.objects.filter(user=request.user).order_by('-datetime')
    form = addMotive()
    context={
        'last_submit': request.session.get('last_submit', '-'),
        'berat': tempat[0].weight,
        'nama': request.user,
        'list_mileage': data_mileage,
        'form': form,
    }
    return render(request, 'showcalories.html', context)

@csrf_exempt
def add_motive(request):    
    if request.method == 'POST':
        form = addMotive(request.POST)
        if form.is_valid():
            sentences = request.POST.get('motive')
            motive = Motive.objects.create(user=request.user, sentences=sentences)
            response = serializers.serialize('json', [motive])
            request.session['last_submit'] = str(datetime.datetime.now())
            return JsonResponse(
                
                    response, safe=False,
                
            )

@csrf_exempt
def get_motive(request):
    if request.method == 'GET':
        data = Motive.objects.all()
        return HttpResponse(serializers.serialize('json', data),
            content_type='application/json'
        )

@csrf_exempt
def get_last_submit(request):
    if request.method == "GET":
        data = request.session.get('last_submit', '-')
        return JsonResponse({'last_submit': data})

def show_json(request):
    data = Motive.objects.all()
    return HttpResponse(serializers.serialize('json', data))


def calories_chart(request):
    date = []
    calories = []

    queryset = Footprint.objects.filter(user=request.user).order_by('-datetime')
    count = 0

    for items in queryset:
        if items.onFoot:
            if count < 7:
                date.append(items.datetime)
                if items.onFoot:
                    calories.append(items.mileage*4057.55263)
                else:
                    calories.append(items.mileage*0)
                count += 1
        
    return JsonResponse(data={
        'date': date,
        'calories': calories,
    })
