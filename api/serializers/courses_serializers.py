from rest_framework import serializers
from courses.models import Category,Course,Module,Rating


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id','title','description','image','status',
            'created','updated','teacher','category','student']
    category = CategorySerializer(many=False)


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['id','title','position','content','video','notes',
        'ppt','created','updated','course','completed']
    course = CourseSerializer(many=False)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id','user','course','rate','review','created','updated']
    course = CourseSerializer(many=False)