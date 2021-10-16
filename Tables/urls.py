from django.urls import path
from . import views

urlpatterns = [
    path('', views.parsing, name='parsing'),
]