from django.urls import path
from . import views
from .views import *
app_name = 'dashboard_moral_person'
urlpatterns = [
    
    path('create_moral/',views.create_moral, name='create_moral'),

    
]