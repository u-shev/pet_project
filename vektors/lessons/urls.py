from django.urls import path
from .views import IndexLessonsView, LessonCreateView, \
    LessonDeleteView, LessonDetailView, LessonUpdateView


urlpatterns = [
    path('', IndexLessonsView.as_view(), name='course'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson'),
    path('create/', LessonCreateView.as_view(), name='create_lesson'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='update_lesson'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='delete_lesson'),
]
