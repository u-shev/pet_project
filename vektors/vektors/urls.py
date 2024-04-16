from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('adminka/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('vektors/', TemplateView.as_view(template_name='vektors.html'),
         name='vektors'),
    path('vektors/about', TemplateView.as_view(
        template_name='vektors_about.html'), name='vektors_about'),
    path('vektors/course_about', TemplateView.as_view(
        template_name='course_about.html'), name='course_about'),
    path('personal_data/', TemplateView.as_view(
        template_name='personal_data_doc.html'), name='personal_data'),
    path('refund/', TemplateView.as_view(template_name='refund.html'),
         name='refund'),

    path('users/', include('users.urls'), name='users'),
    path('vektors/feedback/', include('feedback.urls'), name='feedback'),
    path('vektors/cases/', include('posts.urls'), name='cases'),
    path('vektors/course/', include('lessons.urls'), name='course'),

    path('buy/', TemplateView.as_view(template_name='buy.html'), name='buy'),
    path('buy/pay_for_base/', views.base_pay_view, name='pay_for_base'),
    path('buy/pay_for_standart/', views.standart_pay_view,
         name='pay_for_standart'),
    path('buy/pay_for_full/', views.full_pay_view, name='pay_for_full'),
    path('success_payment/', views.success_payment_view,
         name='success_payment'),
    path('failed_payment/', TemplateView.as_view(
        template_name='failed_payment.html'), name='failed_payment'),
    path('some_secret_result_not_url/', views.result_view,
         name='some_secret_result_not_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
