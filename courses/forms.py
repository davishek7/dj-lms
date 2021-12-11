from django import forms
from .models import Course,Section,Module,Category,Rating
from django_summernote.widgets import SummernoteWidget


class CourseForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, 
                                    empty_label="Select Category", widget=forms.Select(attrs={'class': 'mb-2'}))
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'mb-2'}))
    image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'mb-2'}))
    description = forms.CharField(required=True,widget=SummernoteWidget(attrs={'class':'mb-2',
                                'summernote': {'width': '100%', 'height': '320px'}}),help_text='*Max 1000 characters')
    status = forms.CharField(required=True,widget=forms.Select(
                            choices=Course.options, attrs={'class': 'mb-2'}),
                            help_text='*You can also publish your course later from your profile')
    
    class Meta:
        fields = ['category','title','description','image','status']
        model = Course


class SectionForm(forms.ModelForm):

    order = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'mb-2'}))
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'mb-2'}))

    class Meta:
        fields = ['order','title']
        model = Section


class ModuleForm(forms.ModelForm):

    order = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'mb-2'}))
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'mb-2'}))
    content = forms.CharField(required=True,widget=SummernoteWidget(attrs={'class':'mb-2'}),help_text='*Max 2000 characters')
    video = forms.URLField(required=True,widget=forms.TextInput(attrs={'class':'mb-2'}))

    class Meta:
        fields = ['order','title','content','video']
        model = Module


class RatingForm(forms.ModelForm):
    rate = forms.IntegerField(required=True,widget=forms.Select(choices=Rating.options, attrs={'class': 'mb-2'}))
    review = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Your review','class':'mb-2'}))

    class Meta:
        fields = ['rate','review']
        model = Rating


class SearchForm(forms.Form):
    q = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search for Courses'}),required=True)
