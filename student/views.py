from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from courses.models import Course, Module
from account.models import Student
from account.decorators import student_required


@student_required
@login_required
def student_course_detail_view(request, slug):
    course = get_object_or_404(Course, slug=slug)
    modules = course.course_modules.all()
    first_module = course.course_modules.first()
    context = {'course': course, 'modules': modules,
               'first_module': first_module}
    return render(request, 'student/student_course_detail.html', context)


@student_required
@login_required
def student_module_detail_view(request, course_pk, course_slug, position, slug):

    module = get_object_or_404(Module, course__id=course_pk,
                               course__slug=course_slug, position=position, slug=slug)

    context = {'module': module}

    return render(request, 'student/student_module_detail.html', context)


@student_required
@login_required
def student_enroll_view(request):

    data = {}

    course_id = request.POST.get('course_id')

    if course_id:
        try:
            course = get_object_or_404(Course, id=course_id)
            course.student.add(request.user)

            data['status'] = 'ok'
            data['message'] = 'Start Learning'

            return JsonResponse(data)
        except:
            data['message'] = '404 Not Found'
            return JsonResponse(data)

    data['status'] = 'ko'
    return JsonResponse(data)


@student_required
@login_required
def course_bookmark_view(request):

    course_id = request.POST.get('course_id')
    action = request.POST.get('action')

    if course_id and action:
        try:
            course = get_object_or_404(Course, id=course_id)
            if action == 'add':
                course.bookmarks.add(request.user)
            else:
                course.bookmarks.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            return JsonResponse({'status': '404'})
    return JsonResponse({'status': 'ko'})


@student_required
@login_required
def module_complete_view(request):

    module_id = request.POST.get('module_id')

    if module_id:
        try:
            module = get_object_or_404(Module, id=module_id)
            module.completed.add(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            return JsonResponse({'status': '404'})
    return JsonResponse({'status': 'ko'})
