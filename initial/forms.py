from django import forms
from .models import Letter

class Subme(forms.ModelForm):    
    class Meta:        
        model = Letter   
        fields = ('subEmail', ) 
