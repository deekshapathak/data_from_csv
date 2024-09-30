from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  
    path('data/', views.display_data, name='display_data'),  
]
