from django.urls import path
from . import views

urlpatterns = [
    path('system_info/', views.get_system_info, name='system_info'),
]
