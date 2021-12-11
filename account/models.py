from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course


def user_directory_path(instance, filename):
    return f"profile_pic/{instance.username}/{filename}"
    
    
class User(AbstractUser):

    bio = models.TextField(max_length=500,blank=True)
    image=models.ImageField(upload_to=user_directory_path,default='profile_pic.png', blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class EmailVerificationToken(models.Model):

    user_id = models.IntegerField()
    token = models.CharField(max_length=250,blank=True,null=True)
    created_at = models.IntegerField(null=True)
    updated_at = models.IntegerField(null=True)

    def __str__(self):
        return self.token

    class Meta:
        ordering = ['-created_at']