from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel

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
# Create your views here.                                                           
