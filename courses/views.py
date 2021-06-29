from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Course, Category, Module,Rating
from .forms import CourseForm, ModuleForm, SearchForm,RatingForm
from account.decorators import teacher_required,enrollment_required
from .randomslug import random_slug



def index(request):

    if request.user.is_authenticated:
        if request.user.is_teacher or request.user.is_superuser:
            return redirect('account:teacher_profile')

        if request.user.is_student:
            return redirect('account:student_profile')

    return render(request, 'index.html')


def course_list(request):

    courses_list = Course.objects.filter(status='published')

    page = request.GET.get('page', 1)

    paginator = Paginator(courses_list, 16)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    context = {'courses': courses, 'nbar': 'courses'}
    return render(request, 'courses/course_list.html', context)


def course_details(request, pk, slug):

    course = get_object_or_404(Course, id=pk)

    context = {'course': course}

    return render(request, 'courses/course.html', context)


@teacher_required
@login_required
def course_create(request):

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.slug = slugify(course.title + "-" + random_slug())
            course.teacher = request.user
            course.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f"'{title}' has been added successfully!")
            return HttpResponseRedirect('/course/module/create/'+str(course.id)+'/'+course.slug+'/')
        else:
            messages.warning(
                request, 'Something went wrong! Please try again.')
    else:
        form = CourseForm()
    context = {'form': form, 'nbar': 'course'}

    return render(request, 'courses/add_course.html', context)


@teacher_required
@login_required
def course_update(request, pk, slug):

    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f"'{title}' has been updated successfully!")
            return redirect('account:teacher_profile')
        else:
            messages.warning(
                request, 'Something went wrong! Please try again.')
    else:
        form = CourseForm(instance=course)
    context = {'course': course, 'form': form, 'nbar': 'course'}

    return render(request, 'courses/edit_course.html', context)


@teacher_required
@login_required
def add_modules(request, pk, slug):

    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES)
        if form.is_valid():
            module = form.save(commit=False)
            module.slug = slugify(module.title + "-" + random_slug())
            module.course = course
            module.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f'Module {title} has been added successfully!')
            return HttpResponseRedirect('/course/module/create/'+str(course.id)+'/'+course.slug+'/')
        else:
            messages.warning(
                request, 'Something went wrong! Please try again.')
    else:
        form = ModuleForm()
    context = {'course': course, 'form': form, 'nbar': 'course'}

    return render(request, 'courses/add_modules.html', context)


@teacher_required
@login_required
def edit_modules(request, pk, slug):

    module = get_object_or_404(Module, id=pk)

    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES, instance=module)
        if form.is_valid():
            module = form.save(commit=False)
            module.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Module {title} has been updated successfully!')
            return HttpResponseRedirect('/course/module/create/'+str(module.course.id)+'/'+module.course.slug+'/')
        else:
            messages.warning(
                request, 'Something went wrong! Please try again.')
    else:
        form = ModuleForm(instance=module)
    context = {'module': module, 'form': form, 'nbar': 'course'}

    return render(request, 'courses/edit_modules.html', context)


@login_required
def module_detail(request, pk, slug):

    module = get_object_or_404(Module, id=pk)

    context = {'module': module}

    return render(request, 'courses/module_detail.html')


def category_list(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)
    courses_list = Course.objects.filter(category=category, status='published')

    page = request.GET.get('page', 1)

    paginator = Paginator(courses_list, 16)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    context = {'category': category, 'courses': courses}
    return render(request, 'courses/category_list.html', context)


# @enrollment_required
@login_required
def course_rating(request,pk,slug):
    
    course = get_object_or_404(Course,id=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.course = course
            rating.save()
            messages.success(request,'Thank you for your valuable review.')
            return HttpResponseRedirect('/course/'+str(course.id)+'/'+course.slug+'/')
        else:
            messages.warning(request,'Something went wrong! Please try again later.')
            return HttpResponseRedirect('/course/'+str(course.id)+'/'+course.slug+'/')
    else:
        form = RatingForm()

    context = {'course':course,'form':form}
    return render(request,'courses/course_rating.html',context)


def search(request):

    if 'q' in request.GET:

        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            courses_list = Course.objects.filter(title__icontains=q)
            page = request.GET.get('page', 1)
            paginator = Paginator(courses_list, 16)
            try:
                courses = paginator.page(page)
            except PageNotAnInteger:
                courses = paginator.page(1)
            except EmptyPage:
                courses = paginator.page(paginator.num_pages)

            return render(request, 'courses/search_results.html', {'courses': courses, 'query': q})
