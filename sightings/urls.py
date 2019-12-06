from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<str:squirrel_id>/', views.detail, name='detail'),
]
