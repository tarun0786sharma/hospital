from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_blog/', views.addBlog, name='add_blog'),
    path('view_blog/', views.viewBlogs, name='view_blog'),
    path('my_blog/', views.myBlogs, name='my_blog'),
    path('full_blog/<str:pk>/', views.fullBlog, name='full_blog'),
    path('doctors', views.doctorList, name='doctors'),
    path('new_appointment', views.bookNew, name='new_appointment'),
    path('my_appointment', views.myAppointments, name='my_appointment')
]
