# Generated by Django 3.1.7 on 2021-08-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_auto_20210812_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_app',
            field=models.DateField(),
        ),
    ]