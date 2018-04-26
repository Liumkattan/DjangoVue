from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class welcome(TemplateView):
    template_name = 'welcome.html'


class index(TemplateView):
    template_name = 'index.html'
    
    
class other(TemplateView):
    template_name = 'other.html'