"""
URL Path configuration for flashcard app
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='flashcard'),    # Simple index view for flashcard
    path('study', views.study, name='flashcard_study'),  # Delivers flashcards to user
    # path('results', views.results, name='flashcard_results')   # Delivers results to user

]