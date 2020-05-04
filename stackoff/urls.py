from django.contrib import admin
from django.urls import path,include
from .views import  quest_form_test,initial_page

urlpatterns = [path('hello/',quest_form_test,name='hello'),

               path('',initial_page,name='home')
    
              
]
