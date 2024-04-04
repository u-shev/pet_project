from django.urls import path, include
from .views import UserCreateView, UserConfirmEmailView
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('email-confirmation-sent/', TemplateView.as_view(template_name='registration/email_confirmation_sent.html'), name='email_confirmation_sent'),
    path('email-confirmed/', TemplateView.as_view(template_name='registration/email_confirmed.html'), name='email_confirmed'),
    path('confirm-email-failed/', TemplateView.as_view(template_name='registration/email_confirmation_failed.html'), name='email_confirmation_failed'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
]