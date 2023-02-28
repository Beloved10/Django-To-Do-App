from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.createTask, name='create'),
    path('delete/<int:pk>', views.deleteTask, name='delete'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('register/', views.register, name= 'register'),
    
]