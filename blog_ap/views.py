from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog_ap.models import Person
from blog_ap.services import DataSync

def home(request):
    return render(request=request, template_name="blog_ap/home.html")


def load_data(request):
    return DataSync.fetch_data(request)

def reg_stud_data_page(request):
    return render(request=request, template_name="blog_ap/save_student.html")


def save_data(request):
    return DataSync.save_data(request)


def get_stud_data(request):
    return render(request, template_name="blog_ap/get_student.html")


def register(request):
    form = UserCreationForm()
    return render(request=request, template_name='users/users_reg.html', context={'form': form})