from django.urls import path
from api.views import courses_views as views


urlpatterns = [
    path('',views.CourseList.as_view(),name='listcreate'),
    path('<int:pk>/',views.CourseDetail.as_view(),name='detailcreate'),
    path('<int:pk>/enroll/',views.CourseEnrollView.as_view(),name='course_enroll'),
]