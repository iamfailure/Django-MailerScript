from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def index(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            send_mail('Hello from Siddharth',
    'Hello. You have been registered successfully.This is an automated message. Please reply back answering this "Aur batao swaad aa gaya? Kaisa laga?"','smishra1605@gmail.com',[email],fail_silently=False)
            form.save()

    context = {'form':form}
    return render(request,'index.html',context) 