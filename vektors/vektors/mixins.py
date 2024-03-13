from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class UserLoginRequiredMixin(LoginRequiredMixin):
    auth_message = 'Вы не вошли, пожалуйста, авторизуйтесь'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('account_login'))

        return super().dispatch(request, *args, **kwargs)
