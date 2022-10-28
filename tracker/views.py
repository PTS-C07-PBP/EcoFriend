from datetime import datetime
from tracker.forms import TrackerForm
from tracker.models import Footprint
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# @login_required(login_url='login/')
def tracker(request):
    return render(request, "tracker.html")

def show_history(request):
    history = Footprint.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', history))

def add_footprint(request):
    if request.method == 'POST':
        tracker_form = TrackerForm(request.POST)
        if tracker_form.is_valid():
            user = request.user
            nowvar = datetime.now()
            date_str = nowvar.strftime("%H:%M %b %d, %Y")
            date = datetime.strptime(date_str, "%H:%M %b %d, %Y")
            
            mileage = request.POST.get('mileage')
            type = request.POST.get('btnradio')
            
            carbon = mileage
            to_order = str(int(carbon) / int(mileage))
            on = False
            
            if type == "mobil":
                carbon = str(int(mileage) * 17)
            if type == "jalan":
                carbon = 0
                on = True
            
            # membuat objek baru berdasarkan model dan menyimpannya ke database
            new_footprint = Footprint(user=user, datetime=date, mileage = mileage, carbon = carbon, onFoot = on, datetime_show=date_str, to_order=to_order)
            new_footprint.save()
            
            return render(request, 'tracker.html')
        else:
            tracker_form = TrackerForm()
            messages.info(request, 'PLease fill out all fields to proceed')
    return render(request, 'tracker.html')

# fungsi mendaftarkan pengguna
def register(request):
    # memvalidasi input
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created.')
            return redirect('tracker:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# fungsi melakukan login
def login_user(request):
    # memvalidasi input
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # melakukan login terlebih dahulu
            login(request, user)
            
            # membuat respons
            response = HttpResponseRedirect(reverse("tracker:show_history"))
            
            # membuat cookie last_login dan menambahkannya ke dalam response
            # response.set_cookie("last_login", str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)
    
# fungsi melakukan logout
def logout_user(request):
    logout(request)
    
    # mengembalikan ke halaman awal dan menghapus cookie last_login
    response = HttpResponseRedirect(reverse('tracker:login'))
    return response