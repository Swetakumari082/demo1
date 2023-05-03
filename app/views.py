from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
import django_filters
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def add_course(request):
     return render(request, 'course/add_course.html')

    