from django.contrib import admin
from .models import Course,Category,Module             #Rating,Section
from django_summernote.admin import SummernoteModelAdmin
from .randomslug import random_slug


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

    class Meta:
        model = Category


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ['__str__',]         #'teacher']
    search_fields = ['title', 'teacher__username', 'teacher__email']
    prepopulated_fields={'slug':('title',)}
    summernote_fields = ['description']

    class Meta:
        model = Course


# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ['__str__','title','slug','course']
#     search_fields = ['title', 'course']
#     prepopulated_fields={'slug':('title',)}

#     class Meta:
#         model = Section


@admin.register(Module)
class ModuleAdmin(SummernoteModelAdmin):
    list_display=['__str__','title','slug',]         #'course','section']
    search_fields = ['title',]         # 'course',]                   #'section']
    prepopulated_fields={'slug':('title',)}
    summernote_fields = ['content']

    class Meta:
        model = Module