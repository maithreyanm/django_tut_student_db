from users import views
from django.urls import path



urlpatterns = [
    path('', views.register, name = 'users-register')
    ]