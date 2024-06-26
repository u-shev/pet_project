from django.urls import path
from .views import FeedbackPostCreateView, FeedbackPostDeleteView, \
    FeedbackPostDetailView, FeedbackPostListView, FeedbackPostUpdateView


urlpatterns = [
    path('', FeedbackPostListView.as_view(), name='feedback_posts'),
    path('<int:pk>/', FeedbackPostDetailView.as_view(),
         name='feedback_post'),
    path('create/', FeedbackPostCreateView.as_view(),
         name='create_feedback_post'),
    path('<int:pk>/update/', FeedbackPostUpdateView.as_view(),
         name='update_feedback_post'),
    path('<int:pk>/delete/', FeedbackPostDeleteView.as_view(),
         name='delete_feedback_post'),
]
