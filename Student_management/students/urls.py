from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.publicPage, name='public'),
    path('create_student/', views.createStudent, name='create_student'),
    path('login/', views.studentLogin, name='student_login'),
    path('logout/', views.studentLogout, name='student_logout'),
    path('home/', views.studentHome, name='student_home'),
]
