"""my_gradebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.add_course, name='add_form'),
    path('delete/<slug:course_name>',views.remove_course,name='remove_course'),
    path('edit/<str:course_name>',views.edit_course,name='remove_course')
    
    ]