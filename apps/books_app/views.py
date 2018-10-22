#Add default index routing, e.g.:
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *

def index(request):

    response = "you made it to the logged in book reviews app site."
    #return HttpResponse(response)
    return render(request, 'books_app/index.html')
    #return render(request,'users_app/index.html', {"users": User.objects.all()})

# Create your views here.
