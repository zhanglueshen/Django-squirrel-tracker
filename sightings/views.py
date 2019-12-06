from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel
from .forms import SquirrelForm

def home(request):
    return render(request, 'sightings/home.html')

def sightings(request):
    squirrel_id = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'sightings/sightings.html', {'squirrel_id':squirrel_id})

def detail(request, squirrel_id):
    data = Squirrel.objects.get(squirrel_id=squirrel_id)
    if request.method == "POST":
        if 'delete' in request.POST:
            data.delete()
        else:
            data = SquirrelForm(instance=data,data=request.POST)
            if data.is_valid():
                data.save()
        return redirect('/sightings/sightings/')
    return render(request, 'sightings/detail.html', {'data':data})

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/sightings/")
    else:
        form = SquirrelForm()
    return render(request, 'sightings/add.html', {'form':form})

def stats(request):
    sq_data=Squirrel.objects.all()
    a=len(sq_data)
    b=sq_data.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
    c=sq_data.aggregate(min_longitude=Min('longitude'),max_longitude=Max('longitude'),average_longitude=Avg('longitude'))
    d=list(sq_data.values_list('shift').annotate(Count('shift')))
    e=list(sq_data.values_list('age').annotate(Count('age')))
    f=list(sq_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/stats.html', {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f})
# Create your views here.                                                           
