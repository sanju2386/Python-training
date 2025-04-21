from django.urls import path
from app4 import views

urlpatterns = [
    path('converter/', views.converter, name='converter'),
    path('timer/', views.timer, name='timer'),
]
