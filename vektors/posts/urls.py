from django.urls import path
from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create_posts'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update_posts'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_posts'),
]