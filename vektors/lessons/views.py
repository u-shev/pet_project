from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from vektors.mixins import UserLoginRequiredMixin
from .models import *
from .forms import LessonForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexLessonsView(UserLoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "lessons.view_lesson"
    template_name = 'lessons/index.html'
    model = Lesson
    context_object_name = 'lessons'
    extra_context = {'title': 'ВекторА'}


class LessonCreateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, CreateView):
    permission_required = ("lessons.view_lesson", "lessons.add_lesson")
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


class LessonDetailView(UserLoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "lessons.view_lesson"
    model = Lesson
    template_name = "lessons/lesson.html"
    context_object_name = "lesson"


