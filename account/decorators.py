from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from courses.models import Course


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        if request.user.is_authenticated:
            messages.warning(request,'You are not authorised!')
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func


def teacher_required(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        if request.user.is_student:
            messages.warning(request,'You are not authorised!')
            return redirect('account:student_profile')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func


def student_required(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        if request.user.is_teacher or request.user.is_superuser:
            messages.warning(request,'You are not authorised!')
            return redirect('account:teacher_profile')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func


def enrollment_required(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        course = Course.objects.get(id=kwargs['pk'],slug=kwargs['slug'])

        if request.user not in course.ratings.all():
            messages.warning(request,'You have already rated!')
            return HttpResponseRedirect('/course/'+str(course.id)+'/'+course.slug+'/')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func