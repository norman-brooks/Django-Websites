from django.urls import path
from profiles import views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),  # This should point to the home view
]


