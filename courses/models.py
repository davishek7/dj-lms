from django.db import models
from django.db.models import Avg
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxLengthValidator


def user_directory_path(instance, filename):
    return f"{instance.teacher}/courses/{instance.title}/{filename}"

def upload_lesson_files(instance, filename):
    return f"{instance.course}/module/{instance.title}/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('courses:category_list',args=[self.slug])


class Course(models.Model):

    class CourseObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published')
    )

    user_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=250,blank=True)
    slug = models.SlugField(max_length=250,db_index=True,unique=True)
    image = models.ImageField(upload_to=user_directory_path,default='upload.png',blank=True)
    description = models.TextField(validators=[MaxLengthValidator(1000)],blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=options,default='draft')
    
    objects = models.Manager() 
    courseobjects = CourseObjects()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_details", kwargs={"pk":self.id,"slug": self.slug})

    # @property
    # def average_rating(self):
    #     return self.ratings.all().aggregate(Avg('rate')).get('rate__avg',0.0)

    class Meta:
        ordering = ['-created_at']


class Module(models.Model):
    course_id = models.IntegerField()
    title = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    priority = models.PositiveSmallIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']


class Lesson(models.Model):
    course = models.IntegerField()
    module = models.IntegerField()
    title = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    priority = models.PositiveSmallIntegerField(blank=True,null=True)
    content = models.TextField(validators=[MaxLengthValidator(2000)],blank=True)
    video = models.URLField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_student_detail_url(self):
        return reverse("student:student_module_detail_view", kwargs={'course_pk':self.course.id, 'course_slug':self.course.slug, 
                                                        'order':self.order,'slug': self.slug,})
    class Meta:
        ordering = ['priority']


class CourseRating(models.Model):

    options = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    rating = models.PositiveSmallIntegerField(choices=options)
    review = models.TextField(validators=[MaxLengthValidator(500)],blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s rating on {self.course}"

    class Meta:
        ordering = ['-created_at']


class StudentBookmark(models.Model):
    user_id = models.IntegerField()
    courses = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}'s bookmarks"


class StudentCourseStatus(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    completed_modules = models.TextField()
    completed_lessons = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)