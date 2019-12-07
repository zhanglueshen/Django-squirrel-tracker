from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('sightings/', views.sightings, name='sightings'),
    path('map/', views.map, name='map'),
    path('sightings/add/',views.add,name='add'),
    path('sightings/stats/',views.stats,name='stats'),
    path('sightings/<str:squirrel_id>/', views.edit, name='edit'),
]
