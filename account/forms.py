from django import forms
from django.contrib.auth.models import User
from .models import Profile, Houses, News

class LoginForm(forms.Form):    
    username = forms.CharField()    
    password = forms.CharField(widget=forms.PasswordInput) 

 


class UserRegistrationForm(forms.ModelForm):    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)    
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:        
        model = User       
        fields = ('username', 'first_name', 'email', )

    

    def clean_password2(self):        
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
            return cd['password2']

    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password', 'password2']:
            self.fields[fieldname].help_text = None
 
class UserEditForm(forms.ModelForm):    
    class Meta:        
        model = User        
        fields = ('first_name', 'last_name', 'email')

class SubForm(forms.ModelForm):    
    class Meta:        
        model = News        
        fields = ( 'email',)

class ProfileEditForm(forms.ModelForm):    
    class Meta:        
        model = Profile 
        labels = {
            'City_of_residence': 'City of residence/Intended city of residence',
            'if_student': 'if you are a student, what institution are you in?'
        }       
        fields = ('date_of_birth', 'City_of_residence', 'Type_of_user', 'if_student', 'phone_number', 'gender', 'image')



class ContactForm(forms.Form):
    Your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)