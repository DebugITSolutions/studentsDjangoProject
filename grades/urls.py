from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('students/<int:student_id>/', views.student_dashboard, name='student_dashboard'),
    path('lessons', views.lessons_list, name='lessons_list'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]
