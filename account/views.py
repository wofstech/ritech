from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, SubForm
from django.contrib.auth.decorators import login_required
from .models import Profile, News
from django.contrib import messages
from django.contrib.auth.models import User

from django.db.models import Q
from django.views import generic
from account.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from paystack.signals import payment_verified
from django.dispatch import receiver
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def user_login(request):    
    if request.method == 'POST':        
        form = LoginForm(request.POST)        
        if form.is_valid():            
            cd = form.cleaned_data            
            user = authenticate(username=cd['username'],                                
            password=cd['password'])            
            if user is not None:                
                if user.is_active:                    
                    login(request, user)                    
                    return HttpResponse('Authenticated '\
                'successfully')                
                else:                    
                        return HttpResponse('Disabled account')
            else:                
                        return HttpResponse('Invalid login')    
    else:        
        form = LoginForm()    
        return render(request, 'account/login.html', {'form': form}) 


@login_required 
def dashboard(request):
    profile = Profile.objects.all() 
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'profile': profile}) 

def register(request):    
    if request.method == 'POST':        
        user_form = UserRegistrationForm(request.POST)        
        if user_form.is_valid():            
            # Create a new user object but avoid saving it yet            
            new_user = user_form.save(commit=False)            
            # # Set the chosen password                             
            new_user.set_password(                
            user_form.cleaned_data['password'])            
            # Save the User object            
            new_user.save() 
            profile = Profile.objects.create(user=new_user)            
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            messages.error(request, "Error")
    else:        
         user_form = UserRegistrationForm()    
    return render(request, 'account/register.html', {'user_form': user_form}) 
