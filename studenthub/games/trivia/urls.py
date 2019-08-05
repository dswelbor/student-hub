"""
URL Path configuration for trivia app
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='trivia'),    # Simple index view for trivia
    path('test', views.test, name='trivia_test'),  # Simple view for tests
    path('play', views.play, name='trivia_play'),  # Delivers questions to user
    path('results', views.results, name='trivia_results')   # Delivers questions to user

]
