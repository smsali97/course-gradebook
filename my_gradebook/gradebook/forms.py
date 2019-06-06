from django.forms import ModelForm
from gradebook.models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','course_grade','course_pct','course_semester','course_year','course_credit_hours']
