from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog_ap-home'), #
    path('get_stud_data', views.get_stud_data, name = 'get_stud_data'), #
    path('reg_stud_data', views.reg_stud_data_page, name = 'reg_stud_data'), #
    path('dataLoader', views.load_data, name ='dataLoader'),
    path('dataSaver', views.save_data, name ='dataSaver')
]