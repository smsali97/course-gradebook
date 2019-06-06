from django.db import models

# Create your models here.

grades = {"A" : 4, "A-": 3.67, "B+" : 3.33, "B" : 3.00, "C+" : 2.33, "C" : 2, "C-" : 1.67, "F" : 0}


class Course(models.Model):
    course_name = models.CharField(verbose_name='Course Name',primary_key=True, max_length=50)
    course_grade = models.CharField(verbose_name='Course Grade',max_length=2)
    course_pct = models.DecimalField(decimal_places=2,max_digits=4,verbose_name='Course Percentage')
    course_credit_hours = models.IntegerField(verbose_name='Course Credit Hours')
    course_semester = models.CharField(verbose_name='Course Semester',max_length=15)
    course_year = models.IntegerField()
    course_grade_points = models.DecimalField(decimal_places=2,max_digits=3,verbose_name='Course Grade Points')
    
    def compute_grade_points(self):
        return grades[self.course_grade]
    
    def save(self, *args, **kwargs):
        self.course_grade_points = self.compute_grade_points()
        super(Course, self).save(*args, **kwargs)
        