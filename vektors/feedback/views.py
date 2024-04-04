from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from vektors.mixins import UserLoginRequiredMixin
from .models import FeedbackPost
from .forms import FeedbackPostForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class FeedbackPostListView(ListView):

    template_name = 'feedback/feedback_posts.html'
    model = FeedbackPost
    context_object_name = 'feedback_posts'


class FeedbackPostDetailView(UserLoginRequiredMixin,
                     SuccessMessageMixin, DetailView):
    model = FeedbackPost
    template_name = "feedback/feedback_post.html"
    context_object_name = "feedback_post"


class FeedbackPostCreateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    permission_required = "feedback.add_feedbackpost"
    template_name = 'form.html'
    model = FeedbackPost
    form_class = FeedbackPostForm
    success_url = reverse_lazy('feedback_posts')
    success_message = 'Ваш отзыв опубликован'
    extra_context = {
        'title': 'Оставить отзыв',
        'button_text': 'Опубликовать',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FeedbackPostUpdateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = FeedbackPost
    form_class = FeedbackPostForm
    success_url = reverse_lazy('feedback_posts')
    success_message = 'Отзыв изменен'
    extra_context = {
        'title': 'Изменить отзыв',
        'button_text': 'Изменить',
    }


class FeedbackPostDeleteView(UserLoginRequiredMixin,
                     SuccessMessageMixin, DeleteView):

    template_name = 'feedback/delete.html'
    model = FeedbackPost
    success_url = reverse_lazy('feedback_posts')
    success_message = 'Ваш отзыв удален'
    protected_url = reverse_lazy('feedback_posts')
    extra_context = {
        'title': 'Удалить отзыв',
        'button_text': 'Да, удалить',
    }

