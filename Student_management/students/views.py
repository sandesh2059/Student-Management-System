from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CreateStudentForm
from .models import StudentProfile

# Public page
def publicPage(request):
    return render(request, 'students/public.html')

# Admin-only page to create students
@login_required
@user_passes_test(lambda u: u.is_staff)
def createStudent(request):
    form = CreateStudentForm()
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('create_student')
    return render(request, 'students/create_student.html', {'form': form})

# Student login
def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            messages.error(request, 'Username or password is incorrect.')
    return render(request, 'students/login.html')

# Student logout
@login_required
def studentLogout(request):
    logout(request)
    return redirect('student_login')

# Student home page
@login_required
def studentHome(request):
    return render(request, 'students/student_home.html')
