"""
URL Path configuration for academics apps
"""


from django.urls import path, include

urlpatterns = [
    path('flashcard/', include('academics.flashcard.urls'))

]