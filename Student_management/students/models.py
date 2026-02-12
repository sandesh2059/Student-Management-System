from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"
    



class Course(models.Model):
    name = models.CharField(max_length= 20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course,  related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique= True)

    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.name
    
    
