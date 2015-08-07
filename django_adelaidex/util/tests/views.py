from django.views.generic import TemplateView
import os

class HomeView(TemplateView):
    template_name = 'home.html'
