# Generated by Django 3.1.7 on 2021-08-12 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0013_auto_20210812_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='tp_manager',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'doctor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testmanager_set', to=settings.AUTH_USER_MODEL, verbose_name='Test Manager'),
        ),
    ]
