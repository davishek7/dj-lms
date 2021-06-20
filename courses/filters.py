import django_filters
from django import forms
from .models import Course

class CourseFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(label='',choices=Course.options,widget=forms.Select(attrs={'class':'form-control mr-2'}),empty_label='Select Status')
    class Meta:
        model=Course
        fields=['status']