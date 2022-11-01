from datetime import datetime
from tracker.forms import TrackerForm
from tracker.models import Footprint
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core import serializers
from django.shortcuts import HttpResponse, render

@login_required(login_url='user/login/')
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
            type = request.POST.get('type')
            
            carbon = mileage
            on = False
            
            if type == "mobil":
                carbon = str(int(mileage) * 17)
            if type == "jalan":
                carbon = 0
                on = True
                
            to_order = str(int(carbon) / int(mileage))
            
            # membuat objek baru berdasarkan model dan menyimpannya ke database
            new_footprint = Footprint(user=user, datetime=date, mileage = mileage, carbon = carbon, onFoot = on, datetime_show=date_str, to_order=to_order)
            new_footprint.save()
            
            return render(request, 'tracker.html')
        else:
            tracker_form = TrackerForm()
    return render(request, 'tracker.html')