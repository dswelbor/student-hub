from django.http import HttpResponse
from django.template import loader
from .models import Category, Difficulty, Question, MultipleChoice, TrueFalse
from .constants import ANY_CATEGORY
from .utils import get_question_json, get_questions_json
from django.contrib.auth.decorators import login_required  # Require users to be logged in to access page


@ login_required  # Requires users to be logged in for this view
def index(request):
    """Simple initial index view for trivia app"""
    difficulty_list = Difficulty.objects.all().order_by('-difficulty')
    category_list = Category.objects.all().order_by('category')
    template = loader.get_template('trivia/index.html')
    # Map variables for template to use
    context = {
        'ANY_CATEGORY': ANY_CATEGORY,
        'dif_list': difficulty_list,
        'cat_list': category_list
    }
    return HttpResponse(template.render(context, request))


@ login_required  # Requires users to be logged in for this view
def test(request):
    """This is a simple placeholder view for testing"""
    # return HttpResponse("This is placeholder text: test success.")
    # return HttpResponse(random_question_pool(3, difficulty='easy', category=ANY_CATEGORY))
    # return HttpResponse(Question.custom.get_random_questions(qty=26, difficulty='medium', category=ANY_CATEGORY))
    questions = Question.custom.get_random_questions(qty=26, difficulty='medium', category=ANY_CATEGORY)
    # answers = MultipleChoice.custom.get_questions_options(question[0])
    # return HttpResponse(answers)
    # q_json = get_question_json(questions[0])
    # q_json = get_question_json(Question.objects.get(pk=2))
    # return HttpResponse(q_json)
    questions_json = get_questions_json(questions)
    return HttpResponse(questions_json)


