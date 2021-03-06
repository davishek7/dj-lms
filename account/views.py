from .forms import StudentSignUpForm,TeacherSignUpForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from courses.filters import CourseFilter
from student.filters import StudentCourseFilter
from courses.models import Course
from .models import User, Student, EmailVerificationToken
from .decorators import unauthenticated_user,teacher_required,student_required
from .utils import check_token_expiration


@unauthenticated_user
def student_signup(request):

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_student=True
            user.save()
            student=Student.objects.create(user=user)
            messages.success(request,'Your account has been created successfully. PLease verify your email.')
            return redirect('account:login')
        else:
            messages.warning(request,'Something went wrong! Please try again.')
    else:
        form = StudentSignUpForm()
    context = {'form':form}
    return render(request,'account/student_signup.html',context)


@unauthenticated_user
def teacher_signup(request):

    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_teacher=True
            user.save()
            messages.success(request,'Your account has been created successfully. PLease verify your email.')
            return redirect('account:login')
        else:
            messages.warning(request,'Something went wrong! Please try again.')
    else:
        form = TeacherSignUpForm()
    context = {'form':form}
    return render(request,'account/teacher_signup.html',context)


@unauthenticated_user
def verify_email(request):

    token = request.GET.get('token')

    user_token = EmailVerificationToken.objects.filter(token=token).first()

    if user_token:
        user = User.objects.filter(id=user_token.user_id).first()
        if user.is_active:
            messages.info(request,'User already verified.')
            return redirect('account:login')
        elif check_token_expiration(user_token) > 60:
            messages.warning(request,'Token expired.')
            return redirect('account:login')            
        else:
            user.is_active = True
            user.save()
            messages.success(request,'Email verified successfully. You can login now.')
            return redirect('account:login')
    else:
        messages.warning(request,'Invalid token.')

    return render(request,'account/verification.html')


@teacher_required
@login_required
def teacher_profile(request):

    courses_list = Course.objects.filter(teacher=request.user,status='published')

    myFilter=CourseFilter(request.GET,queryset=courses_list)
    courses_list=myFilter.qs

    page = request.GET.get('page', 1)

    paginator = Paginator(courses_list, 6)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Profile has been updated successfully!')
            return redirect('account:teacher_profile')
        else:
            messages.warning(request,'Something went wrong! Please try again later.')
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    context = {'u_form':u_form,'courses':courses,'myFilter':myFilter}
    return render(request,'account/teacher_profile.html',context)


@student_required
@login_required
def student_profile(request):

    courses_list = Course.objects.filter(student=request.user,status='published')

    myFilter=StudentCourseFilter(request.GET,queryset=courses_list)
    courses_list=myFilter.qs

    page = request.GET.get('page', 1)

    paginator = Paginator(courses_list, 6)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Profile has been updated successfully!')
            return redirect('account:student_profile')
        else:
            messages.warning(request,'Something went wrong! Please try again later.')
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    context = {'u_form':u_form,'courses':courses,'myFilter':myFilter}
    return render(request,'account/student_profile.html',context)


