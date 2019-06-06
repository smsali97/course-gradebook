from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .forms import CourseForm
from .models import Course
from django.db.models import Sum, F, FloatField

# Create your views here.


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = CourseForm()
    courses = Course.objects.all()
    
    total_credit_hours = Course.objects.aggregate(total_credit_hours=Sum(F('course_credit_hours')))['total_credit_hours']
    total_grade_points = Course.objects.aggregate(total_grade_points=Sum(F('course_grade_points')*F('course_credit_hours'),output_field=FloatField()))['total_grade_points']
    total_percentage = Course.objects.aggregate(total_percentage=Sum(F('course_pct')*F('course_credit_hours'),output_field=FloatField()))['total_percentage']
    
    
    
    cgpa = round(total_grade_points / total_credit_hours,3)
    pct = round(total_percentage / total_credit_hours,2)
    
    
    return render(request,'add_course.html',{'form':form, 'courses' : courses, 'cgpa': cgpa, 'pct' : pct})

def remove_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    
    form = CourseForm()
    courses = Course.objects.all()
    return render(request,'add_course.html',{'form':form, 'courses' : courses})
