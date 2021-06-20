from django.urls import path
from . import views

app_name='student'

urlpatterns = [
    path('course/enroll/',views.student_enroll_view,name='student_enroll_view'),
    path('course/details/<slug:slug>/',views.student_course_detail_view,name='student_course_detail_view'),
    path('module/details/<int:course_pk>/<slug:course_slug>/module/<int:position>/<slug:slug>/',views.student_module_detail_view,name='student_module_detail_view'), 
    path('course/bookmark/',views.course_bookmark_view,name='course_bookmark_view'),
    path('module/completed/',views.module_complete_view,name='module_complete_view'),
]
