from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adminka/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('vektors/', TemplateView.as_view(template_name='vektors.html'), name='vektors'),
    path('buy/', TemplateView.as_view(template_name='buy.html'), name='buy'),
    path('vektors/about', TemplateView.as_view(template_name='vektors_about.html'), name='vektors_about'),
    path('vektors/course_about', TemplateView.as_view(template_name='course_about.html'), name='course_about'),
    path('personal_data/', TemplateView.as_view(template_name='personal_data_doc.html'), name='personal_data'),
    path('refund/', TemplateView.as_view(template_name='refund.html'), name='refund'),

    path('users/', include('users.urls'), name='users'),
    path('vektors/feedback/', include('feedback.urls'), name='feedback'),
    path('vektors/cases/', include('posts.urls'), name='cases'),
    path('vektors/course/', include('lessons.urls'), name='course'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)