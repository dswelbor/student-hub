"""
URL Path configuration for trivia app
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index')

]