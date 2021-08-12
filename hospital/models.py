from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    Categories = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('COVID-19', 'COVID-19'),
        ('Immunization', 'Immunization'),
    )
    title = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=200, null=False, choices=Categories)
    summary = models.CharField(max_length=200, null=False)
    content = models.CharField(max_length=2000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"


class Appointment(models.Model):
    Special = (
        ('Eye Surgery', 'Eye Surgery'),
        ('General Surgery', 'General Surgery'),
        ('Dentist', 'Dentist'),
        ('Physician', 'Physician'),
    )

    time_app = (
        ('10:00 AM - 10:45 AM', '10:00 AM - 10:45 AM'),
        ('12:00 PM - 12:45 PM', '12:00 PM - 12:45 PM'),
        ('02:30 PM - 03:15 PM', '02:30 PM - 03:15 PM'),
        ('04:15 PM - 05:00 PM', '04:15 PM - 05:00 PM'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.CharField(max_length=200, null=False, choices=Special, verbose_name='Speciality',)
    timings = models.CharField(max_length=200, null=False, choices=time_app, verbose_name='Time',)
    date_app = models.DateField(null=False, verbose_name='Date',)
    Doctor = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, verbose_name='Doctor',
                                   limit_choices_to={'groups__name': 'doctor'},
                                   related_name='testmanager_set')

    def __str__(self):
        return self.category




