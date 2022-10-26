import datetime
from tracker.models import Footprint
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='login/')
def tracker(request):
    return render(request, "tracker.html")

def show_history(request):
    history = Footprint.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', history))

# def show_history(request):
#     history = Footprint.objects.filter(user=request.user)
#     context = {
#          # "list_task": data_task_item,
#         "task_user" : request.user,
#         "last_login": request.COOKIES['last_login']
#     }
#     return render(request, "todolist.html", context)

def add_footprint(request):
    if request.method == 'POST':
        user = request.user
        date = datetime.datetime.now()
        mileage = request.POST.get('mileage')
        # type = request.POST['btnradio']
        type = request.POST.get('btnradio')
        carbon = mileage
        on = False
        if type == "mobil":
            carbon = carbon*17
        elif type == "jalan":
            carbon = 0
            on = True
        
        # membuat objek baru berdasarkan model dan menyimpannya ke database
        new_footprint = Footprint(user=user, date = date, mileage = mileage, carbon = carbon, onFoot = on)
        new_footprint.save()
        
        context = {
            "task_user" : request.user,
            "last_login": request.COOKIES['last_login']  
        }
        return render(request, 'tracker.html', context) 

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
    response.delete_cookie('last_login')
    return response