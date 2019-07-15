from django.http import HttpResponse


def index(request):
    return HttpResponse("This is placeholder text: django-based ui for trivia game app.")