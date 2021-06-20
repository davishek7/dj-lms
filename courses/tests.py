from django.test import TestCase
from .models import Course,Category
from django.conf import settings
from account.models import User


class CourseTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = 'abc',password='password')
        self.category=Category.objects.create(name='test',slug='test')
        Course.objects.create(category=self.category,teacher=self.user,title='Course1',slug='course1',description='course1')
    
    # def test_course_created(self):
    #     category2=Category.objects.create(name='test1',slug='test1')
    #     course2 = Course.objects.create(category=category2,teacher=self.user,title='Course2',slug='course2',description='course2')
    #     self.assertEqual(course2.id,2)
    #     self.assertEqual(course2.teacher,self.user)
    #     self.assertEqual(course2.category,category2)

    def test_category_list(self):
        
        course2 = Course.objects.create(category=self.category,teacher=self.user,title='Course2',slug='course2',description='course2')
        course3 = Course.objects.create(category=self.category,teacher=self.user,title='Course3',slug='course3',description='course2')
        course4 = Course.objects.create(category=self.category,teacher=self.user,title='Course4',slug='course4',description='course2')

        courses = Course.objects.filter(category = self.category)

        self.assertEqual(courses.count(),4)