from django.views.generic import TemplateView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'title': 'ВекторА'}


class VektorsView(TemplateView):
    template_name = 'vektors.html'
    extra_context = {'title': 'ВекторА'}


class VektorsAboutView(TemplateView):
    template_name = 'vektors_about.html'
    extra_context = {'title': 'ВекторА'}


class BuyView(TemplateView):
    template_name = 'buy.html'
    extra_context = {'title': 'ВекторА'}
