from django import forms
from .models import FeedbackPost


class FeedbackPostForm(forms.ModelForm):

    class Meta:
        model = FeedbackPost
        fields = ('author', 'description')