"""
URL Path configuration for trivia app
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='trivia'),    # Simple index view for trivia
    path('test', views.test, name='trivia_test')       # Simple view for tests

]
