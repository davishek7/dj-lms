from .forms import LoginForm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',form_class=LoginForm, 
    redirect_authenticated_user=True,), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='account:login'), name='logout'),
    path('signup/student/', views.student_signup, name='student_signup'),
    path('signup/teacher/', views.teacher_signup, name='teacher_signup'),
    path('teacher/profile/',views.teacher_profile,name='teacher_profile'),
    path('student/profile/',views.student_profile,name='student_profile'),
]