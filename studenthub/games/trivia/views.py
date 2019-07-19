from django.http import HttpResponse
from django.template import loader
from .models import Category, Difficulty
from django.contrib.auth.decorators import login_required  # Require users to be logged in to access page


@ login_required  # Requires users to be logged in for this view
def index(request):
    """Simple initial index view for trivia app"""
    difficulty_list = Difficulty.objects.all()
    category_list = Category.objects.all()
    template = loader.get_template('trivia/index.html')
    # Map variables for template to use
    context = {
        'dif_list': difficulty_list,
        'cat_list': category_list
    }
    return HttpResponse(template.render(context, request))


@ login_required  # Requires users to be logged in for this view
def test(request):
    """This is a simple placeholder view for testing"""
    # TODO: Map this in urls.py
    return HttpResponse("This is placeholder text: test success.")
