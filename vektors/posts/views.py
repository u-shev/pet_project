from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from vektors.mixins import UserLoginRequiredMixin
from .models import Post
from .forms import PostForm

class PostListView(ListView):

    template_name = 'posts/posts.html'
    model = Post
    context_object_name = 'posts'
    extra_context = {
        'title': 'Посты',
        'button_text': 'Показать',
    }


class PostDetailView(SuccessMessageMixin, DetailView):
    model = Post
    template_name = "posts/post.html"
    context_object_name = "post"
    extra_context = {'title': 'Отзыв',
                     'btn_update': 'Изменить',
                     'btn_delete': 'Удалить',
                     }


class PostCreateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    success_message = 'Ваш отзыв опубликован'
    extra_context = {
        'title': 'Написать пост',
        'button_text': 'Опубликовать',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    success_message = 'Отзыв изменен'
    extra_context = {
        'title': 'Изменить пост',
        'button_text': 'Изменить',
    }


class PostDeleteView(UserLoginRequiredMixin,
                     SuccessMessageMixin, DeleteView):

    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts')
    success_message = 'Пост удален'
    protected_url = reverse_lazy('posts')
    extra_context = {
        'title': 'Удалить пост',
        'button_text': 'Да, удалить',
    }