import django_filters
from django import forms
from courses.models import Course,Category

class StudentCourseFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(label='',queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control mr-2'}),empty_label='Select Category')

    class Meta:
        model=Course
        fields=['category']