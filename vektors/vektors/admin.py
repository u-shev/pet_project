from django.contrib import admin
from vektors.users.models import User
from vektors.posts.models import Post
from vektors.feedback.models import FeedbackPost

admin.site.register(User)
admin.site.register(Post)
admin.site.register(FeedbackPost)
