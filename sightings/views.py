from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q, Avg, Max, Min, Count

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

def edit(request, squirrel_id):
	squirrel = get_object_or_404(Squirrel,squirrel_id=squirrel_id)
	if request.method=='Post':
		form = SquirrelForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sighting/{squirrel_id}')
	else:
		form = SquirrelForm(instance=squirrel)
	context ={
		'form':form
			}
	return render(request, 'sightings/edit.html', context)


def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/sightings')

    else:
        form = SquirrelForm()

    context = {
            'form': form,}

    return render(request, 'sightings/add.html', context)

def stats(request):
    sq_data=Squirrel.objects.all()
    a=len(sq_data)
    b=sq_data.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
    c=sq_data.aggregate(min_longitude=Min('longitude'),max_longitude=Max('longitude'),average_longitude=Avg('longitude'))
    d=list(sq_data.values_list('shift').annotate(Count('shift')))
    e=list(sq_data.values_list('age').annotate(Count('age')))
    f=list(sq_data.values_list('color').annotate(Count('color')))
    return render(request, 'sightings/stats.html', {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f})

def map(request):
    sightings = Squirrel.objects.all()[:100]
    return render(request, 'sightings/map.html', {'sightings':sightings})

# Create your views here.                                                           
