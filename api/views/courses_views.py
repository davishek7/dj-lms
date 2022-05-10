from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.permissions import IsEnrolled
from courses.models import Course,Category,Module       #,Rating
from api.serializers.courses_serializers import CourseSerializer,CategorySerializer, ModuleSerializer      #,RatingSerializer



class CourseList(generics.ListAPIView):
    queryset = Course.courseobjects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.courseobjects.all()
    serializer_class = CourseSerializer


class CourseEnrollView(APIView):
    queryset = Course.courseobjects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated, IsEnrolled]

    def post(self,request,pk,format = None):
        course = get_object_or_404(Course, id=pk)
        course.student.add(request.user)
        return Response({'enrolled': True})

