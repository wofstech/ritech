from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about-us/$', views.about, name='about-us'),
    
    
    
]