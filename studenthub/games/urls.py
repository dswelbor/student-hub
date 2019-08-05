"""
URL Path configuration for game apps
"""


from django.urls import path, include

urlpatterns = [
    path('trivia/', include('games.trivia.urls'))

]