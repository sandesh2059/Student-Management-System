from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class CreateStudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'course', 'year']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        profile = super().save(commit=False)
        profile.user = user
        if commit:
            profile.save()
        return profile
