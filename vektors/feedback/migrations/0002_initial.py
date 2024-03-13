# Generated by Django 4.2.11 on 2024-03-12 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
    ]
