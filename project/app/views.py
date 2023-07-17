from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from .models.Academic import Academic
from .models.Assignment import Assignment
from .models.Course import Course 
from .models.Department import Department 
from .models.Enroll import Enroll 
from .models.Faculty import Faculty 
from .models.Group import Group 
from .models.Organization import Organization 
from .models.Plan import Plan 
from .models.School import School 
from .models.Semester import Semester 
from .models.Student import Student
from .models.User import User
from .models.User_Type import User_Type
from .models.Teacher import Teacher 
# Create your views here.
class EnrollListView(generic.ListView):
    model = Enroll

class EnrollCreate(CreateView):
    model = Enroll
    fields = '__all__'

class EnrollUpdate(UpdateView):
    model = Enroll
    fields = '__all__'

#class EnrollDelete(DeleteView):
#    model=Enroll
#    success_url= reverse_lazy('enrolls')