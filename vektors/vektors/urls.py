from django.contrib import admin
from django.urls import path, include
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static
from vektors import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('vektors/', VektorsView.as_view(), name='vektors'),
    path('buy/', views.BuyView.as_view(), name='buy'),
    path('vektors/about', VektorsAboutView.as_view(), name='vektors_about'),

    path('vektors/feedback/', include('feedback.urls'), name='feedback'),
    path('vektors/cases/', include('posts.urls'), name='cases'),
    path('vektors/course/', include('lessons.urls'), name='course'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)