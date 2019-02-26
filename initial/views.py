from django.shortcuts import render, redirect
from . models import Letter
from . forms import Subme
from django.contrib import messages

def home(request): 
    if request.method == 'POST': 
        sub_form = Subme(request.POST )
        if sub_form.is_valid():    
            sub = sub_form.save(commit=False)
            sub.save()
            messages.success(request, 'Thanks for subscribing')
            return redirect('home')           
    else:        
        sub_form = Subme()
    return render(request, 'initial/home.html', {'sub_form': sub_form})

def about(request):    
    return render(request, 'initial/about.html')



