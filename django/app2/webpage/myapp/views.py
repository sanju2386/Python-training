from django.shortcuts import render
from django.http import HttpResponse

# View for the Home Page
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

# View for the Index Page
def index(request):
    return HttpResponse("<h1>This is the Index Page!</h1>")
