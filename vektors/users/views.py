
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from vektors.mixins import UserIsNotAuthenticated
from vektors.tasks import send_activate_email_message_task
from .forms import UserForm
from .models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, View
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login


class UserCreateView(SuccessMessageMixin, UserIsNotAuthenticated, CreateView):

    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Зарегистрироваться',
    }

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_activate_email_message_task.delay(user.id)
        return redirect('email_confirmation_sent')


class LogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')
    success_message = 'Вы вышли'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы вышли')
        return super().dispatch(request, *args, **kwargs)


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(
          user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('email_confirmed')
        else:
            return redirect('email_confirmation_failed')
