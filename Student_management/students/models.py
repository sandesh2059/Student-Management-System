from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    grade = models.CharField(max_length = 10)
    courses = models.ManyToManyField(Course, many = True )

    def __str__(self):
        return self.user.username
    
class Course(models.Model):
    name = models.CharField(max_length = 15)
    teacher = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name