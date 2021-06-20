from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'mb-2','placeholder':'Your Username or Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'mb-2','placeholder': 'Your Password'}))


class StudentSignUpForm(UserCreationForm):

    username = forms.CharField(label='Username',min_length=4,max_length=10,widget=forms.TextInput())

    email = forms.EmailField(label='Email', max_length=100,widget=forms.EmailInput())

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())

    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError('Username already exists!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An user with that email already exists, please use another one.')
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('Passwords do not match!')
        return cd['password2']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class':'mb-3','placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Last Name'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Repeat Password'})


class TeacherSignUpForm(UserCreationForm):

    username = forms.CharField(label='Username',min_length=4,max_length=10,widget=forms.TextInput())

    email = forms.EmailField(label='Email', max_length=100,widget=forms.EmailInput())

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())

    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError('Username already exists!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An user with that email already exists, please use another one.')
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('Passwords do not match!')
        return cd['password2']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class':'mb-3','placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Last Name'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'mb-3', 'placeholder': 'Repeat Password'})


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'mb-2','readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'mb-2','readonly': 'readonly'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'mb-2',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'mb-2',}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'mb-2','rows': 5}))
    image=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'mb-2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','bio','image']