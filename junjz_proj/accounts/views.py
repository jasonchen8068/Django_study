from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(req):
    username = 'jasonchen'
    return render(req, "accounts/index.html", {"username":username})

def register(req):
    '''zhuceshitu'''
    if req.method == "POST":
        #zhucewanbi zhijiedenglu
        return HttpResponseRedirect("/accounts/index")
    return render(req, "accounts/register.html")

def login(req):
    '''denglushitu'''
    template_var = {}
    if req.method == 'POST':
        username = req.POST.get("username")
        template_var = {"error": "must first register", "username":username}
    return render(req, "accounts/login.html", template_var,)

def logout(req):
    return render(req, 'accounts/logout.html',) 
