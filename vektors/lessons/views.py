from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from vektors.mixins import UserLoginRequiredMixin
from .models import Lesson
from .forms import LessonForm


class IndexLessonsView(UserLoginRequiredMixin, TemplateView):
    template_name = 'lessons/index.html'
    extra_context = {'title': 'ВекторА'}


class LessonCreateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Lesson
    form_class = LessonForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class LessonUpdateView(UserLoginRequiredMixin, UpdateView):

    template_name = 'form.html'
    model = Lesson
    form_class = LessonForm


class LessonDeleteView(UserLoginRequiredMixin, DeleteView):

    model = Lesson


class LessonDetailView(UserLoginRequiredMixin, DetailView):
    model = Lesson
    template_name = "lessons/lesson.html"
    context_object_name = "lesson"


