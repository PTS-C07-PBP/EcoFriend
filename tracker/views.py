from datetime import datetime
from tracker.forms import TrackerForm
from tracker.models import Footprint
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def tracker(request):
    return render(request, "tracker.html")

@login_required(login_url='/user/login/')
def show_json(request):
    history = Footprint.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', history), content_type='application/json')

@login_required(login_url='/user/login/')
def add_footprint(request):
    if request.method == 'POST':
        tracker_form = TrackerForm(request.POST)
        
        if tracker_form.is_valid():
            user = request.user
            nowvar = datetime.now()
            date_str = nowvar.strftime("%H:%M %b %d, %Y")
            
            mileage = request.POST.get('mileage')
            type = request.POST.get('type')
            
            carbon = 0
            on = False
            
            if type == "mobil":
                carbon = str(float(mileage) * 120)
            if type == "motor":
                carbon = str(float(mileage) * 113)
            if type == "jalan":
                on = True
                
            to_order = str(float(carbon) / float(mileage))
            
            # membuat objek baru berdasarkan model dan menyimpannya ke database
            new_footprint = Footprint(user=user, datetime=nowvar, mileage = mileage, carbon = carbon, onFoot = on, datetime_show=date_str, to_order=to_order)
            new_footprint.save()
            

            return JsonResponse(len(Footprint.objects.filter(user=request.user)), safe=False)
    return HttpResponse('')
