"""
URL Path configuration for StudentHub home
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # Simple index view for trivia
    # path('test', views.test, name='test')       # Simple view for tests

]
