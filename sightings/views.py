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
        dataset = Squirrel.objects \
        .values('sq') \
            .annotate(running_count=Count('sq', filter=Q(running=True)),
                not_running_count=Count('sq', filter=Q(running=False)),
                chasing_count=Count('sq', filter=Q(chasing=True)),
                not_chasing_count=Count('sq', filter=Q(chasing=False)),
                climbing_count=Count('sq', filter=Q(climbing=True)),
                not_climbing_count=Count('sq', filter=Q(climbing=False)),
                eating_count=Count('sq', filter=Q(eating=True)),
                not_eating_count=Count('sq', filter=Q(eating=False)),
                foraging_count=Count('sq', filter=Q(foraging=True)),
                not_foraging_count=Count('sq', filter=Q(foraging=False))) \
        .order_by('sq')
    return render(request, 'sightings/stats.html', {'dataset': dataset})
# Create your views here.                                                           
