from django.contrib import admin
from .models import Lesson, LessonAdditionalPicture, \
    LessonAdditionalVideo


admin.site.register(Lesson)
admin.site.register(LessonAdditionalPicture)
admin.site.register(LessonAdditionalVideo)
