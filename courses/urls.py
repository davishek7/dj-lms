from django.urls import path
from . import views

app_name='courses'

urlpatterns = [
    path('',views.index,name='index'),
    path('courses/',views.course_list,name='all_courses'),
    path('search/',views.search, name='search'),
    path('course/create/',views.course_create,name='course_create'),
    path('course/<str:pk>/<slug:slug>/',views.course_details,name='course_details'),
    path('course/update/<str:pk>/<slug:slug>/',views.course_update,name='course_update'),
    path('course/module/create/<str:pk>/<slug:slug>/',views.add_modules,name='add_modules'),
    path('course/module/edit/<str:pk>/<slug:slug>/',views.edit_modules,name='edit_modules'),
    path('course/rate/<str:pk>/<slug:slug>/',views.course_rating,name='course_rating'),
    path('category/<slug:category_slug>/',views.category_list,name='category_list'),
]
