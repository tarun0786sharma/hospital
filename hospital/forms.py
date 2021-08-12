from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Blog, Appointment
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.get_full_name()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }
        fields = '__all__'
        exclude = ('user', 'img', )


class AppointmentForm(forms.ModelForm):
    Doctor = CustomUserChoiceField(queryset=User.objects.filter(groups__name__in=['doctor']))
    class Meta:
        model = Appointment
        widgets = {
            'date_app': DateInput(),
        }
        fields = '__all__'

        exclude = ('user', )