import django_filters
from .models import *


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['title', 'summary', 'content', 'user', 'image', 'img']
