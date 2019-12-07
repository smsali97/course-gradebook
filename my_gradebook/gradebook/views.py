from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import CourseForm
from .models import Course
from django.db.models import Sum, F, FloatField

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = CourseForm()
    courses = Course.objects.order_by('course_year', '-course_semester', 'course_name')
    
    total_credit_hours = Course.objects.aggregate(total_credit_hours=Sum(F('course_credit_hours')))['total_credit_hours']
    total_grade_points = Course.objects.aggregate(total_grade_points=Sum(F('course_grade_points')*F('course_credit_hours'),output_field=FloatField()))['total_grade_points']
    total_percentage = Course.objects.aggregate(total_percentage=Sum(F('course_pct')*F('course_credit_hours'),output_field=FloatField()))['total_percentage']
    
    
    if total_credit_hours is None:
        cgpa = 'N/A'
        pct = '0'
    else:       
        cgpa = round(total_grade_points / total_credit_hours,4)
        pct = round(total_percentage / total_credit_hours,2)
        
    
    return render(request,'index.html',{'form':form, 'courses' : courses, 'cgpa': cgpa, 'pct' : pct})

def remove_course(request, course_name):
    course = get_object_or_404(Course, pk=course_name)
    course.delete()
    return HttpResponseRedirect(reverse('index'))
def edit_course(request, course_name):
    course = get_object_or_404(Course, pk=course_name)
    if request.method == 'POST':
        course.delete()
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        updatedForm = CourseForm(instance=course)    
    form = CourseForm()



    courses = Course.objects.order_by('course_year', '-course_semester', 'course_name')
    total_credit_hours = Course.objects.aggregate(total_credit_hours=Sum(F('course_credit_hours')))['total_credit_hours']
    total_grade_points = Course.objects.aggregate(total_grade_points=Sum(F('course_grade_points')*F('course_credit_hours'),output_field=FloatField()))['total_grade_points']
    total_percentage = Course.objects.aggregate(total_percentage=Sum(F('course_pct')*F('course_credit_hours'),output_field=FloatField()))['total_percentage']
    
    
    if total_credit_hours is None:
        cgpa = 'N/A'
        pct = '0'
    else:       
        cgpa = round(total_grade_points / total_credit_hours,4)
        pct = round(total_percentage / total_credit_hours,2)

    if request.method == 'POST': 
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'index.html',{'form':form, 'courses' : courses, 'cgpa': cgpa, 'pct' : pct, 'updatedForm' : updatedForm})
        
