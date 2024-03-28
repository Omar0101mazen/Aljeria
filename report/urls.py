from django.urls import path
from . import views
from .views import *
app_name = 'report'
urlpatterns = [
    
    path('list/',views.list, name='list'),
    path('<str:slug>',views.details, name='details'),

    
]