from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
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
    sightings_stats1=Squirrel.objects.all().count()
    sightings_stats2=Squirrel.objects.filter(shift='AM').count()
    sightings_stats3=Squirrel.objects.filter(shift='PM').count()
    sightings_stats4=Squirrel.objects.filter(age='Adult').count()
    sightings_stats5=Squirrel.objects.filter(age='Juvenile').count()
    context={'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    return render(request, 'sightings/map.html', {'sightings':sightings})

# Create your views here.                                                           
