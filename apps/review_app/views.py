from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt

from .models import *

def index(request):
    return render(request, 'review_app/index.html')

def create(request):
    ### Put it all into session so the user won't have to retype it.
    request.session.clear()

    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email_address'] = request.POST['email_address']
    request.session['alias'] = request.POST['alias']


    ### check on duplicate email address
    if User.objects.filter(email_address = request.POST['email_address']):
        messages.add_message(
            request, messages.ERROR,
            'This email address is already in use.  Please log in.'
        )

        return redirect('/')

    ### validate the form submission
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    #create the user record        
    else:
        #hash the password
        passhash = bcrypt.hashpw(request.POST['password1'].encode(), bcrypt.gensalt())

        #create the user
        new_user = User.objects.create(first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email_address = request.POST['email_address'],
            alias = request.POST['alias'],
            password = passhash)

        print(new_user.id)
        request.session.clear()
        request.session['user_id'] = new_user.id

        return render(request, 'review_app/debug.html')


def reset(request):
    request.session.clear()
    return redirect('/')
