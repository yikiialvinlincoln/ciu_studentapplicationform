from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('success/', views.success, name='success'),
]
