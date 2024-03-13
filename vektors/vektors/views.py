from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm


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


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('vektors')
    success_message = 'Вы вошли'
    extra_context = {
        'title': 'Авторизация',
        'button_text': 'Войти',
    }


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('vektors')
    success_message = 'Вы вышли'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы вышли')
        return super().dispatch(request, *args, **kwargs)