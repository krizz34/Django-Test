from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('form/', views.create, name='form'),
    path('read/', views.read, name='readData'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('', views.signUp, name='signUp'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('search/', views.search, name='search'),

]
