from django.contrib import admin
from .models import Course,Category,Module,Rating
from django_summernote.admin import SummernoteModelAdmin
from .randomslug import random_slug


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

    class Meta:
        model = Category

class CourseAdmin(SummernoteModelAdmin):
    list_display = ['__str__','teacher']
    search_fields = ['title', 'teacher__username', 'teacher__email']
    prepopulated_fields={'slug':('title',)}
    summernote_fields = ['description']

    class Meta:
        model = Course

class ModuleAdmin(SummernoteModelAdmin):
    list_display=['__str__','title','slug','course',]
    prepopulated_fields={'slug':('title',)}
    summernote_fields = ['content']

    class Meta:
        model = Module


admin.site.register(Course, CourseAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Rating)
