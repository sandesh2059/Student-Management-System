from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"
