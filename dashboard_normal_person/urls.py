from django.urls import path
from . import views
from .views import *
app_name = 'dashboard_normal_person'
urlpatterns = [
    
    path('create_normal/',views.create_normal, name='create_normal'),

    
]