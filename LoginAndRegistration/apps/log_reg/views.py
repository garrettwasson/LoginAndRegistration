# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "log_reg/index.html")
# Create your views here.

def create(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    
    else:
        this_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        this_user.save()
        request.session['first_name']=this_user.first_name
        return redirect('/success')

        

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        post_password = request.POST['password']
        post_email = request.POST["email"]

            
def success(request):
    
    context = {
        'user' : User.objects.all()
    }
    return render(request, "log_reg/success.html", context)

def clear(request):
    request.session.clear()
    return redirect('/')