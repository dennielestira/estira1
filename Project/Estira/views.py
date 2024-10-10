from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'Estira/home.html'
class AboutPageView(TemplateView):
    template_name = 'Estira/about.html'
class SkillsPageView(TemplateView):
    template_name = 'Estira/skills.html'