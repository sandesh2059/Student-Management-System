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
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)

    course = models.ManyToManyField(Course,  related_name='students')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique= True)

    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.name
    
    
