from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Code added during video 10
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('<int:pk>/details/', views.details, name="details"),

]