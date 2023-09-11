from django.urls import path
from . import views

urlpatterns = [
    path('generate_json/', views.generate_json, name='generate_json'),
]
