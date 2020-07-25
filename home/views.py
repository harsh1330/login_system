from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return HttpResponse("Login")

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={
        'form' : form
    }
    return render(request, 'register.html', context)