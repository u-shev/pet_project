from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        email = forms.EmailField(required=True)
        model = User
        fields = ('email', 'username', 'password1', 'password2'
                  )
