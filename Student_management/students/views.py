from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Student, Teacher
from .serializers import CourseSerializer, StudentSerializer, TeacherSerializer


class CourseCreateAPI(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
