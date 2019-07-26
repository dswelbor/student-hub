from django.http import HttpResponse
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError

from .models import Category, Difficulty, Question, MultipleChoice, TrueFalse, Score
from .constants import ANY_CATEGORY, BOOLEAN, MULTIPLE_CHOICE
from .utils import get_question_json, get_questions_json
from django.contrib.auth.decorators import login_required  # Require users to be logged in to access page


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


@ login_required
def play(request):
    """This view delivers the random samples to the user based on criteria selection"""
    # html template for view
    template = loader.get_template('trivia/play.html')

    # TODO: encapsulate in a try block, on except key exception, redirect to index
    # question parameters
    qty = int(request.POST['qty-questions'])
    difficulty = request.POST['dif-questions']
    category = request.POST['cat-questions']

    # get random questions matching parameters
    questions = Question.custom.get_random_questions(qty=qty, difficulty=difficulty, category=category)
    # get list of questions as json
    questions_json = get_questions_json(questions)

    # Record game start in Score model in db
    this_user = request.user
    this_difficulty = Difficulty.objects.get(difficulty=difficulty)
    game_pk = Score.custom.start(user=this_user, difficulty=this_difficulty)

    # Map variables for template to use
    context = {
        'qty': len(questions_json),  # Accommodate less question in pool than passed qty
        'difficulty': difficulty,
        'category': category,
        'questions_json': questions_json,
        'game_pk': game_pk
        # TODO: Add variables to feed js prototpes data
    }

    return HttpResponse(template.render(context, request))

@login_required
def results(request):
    """
    This view checks requests answers against correct answer attributes in the
    Trivia model and dynamically returns the results to the user.
    """
    # html template for view
    template = loader.get_template('trivia/results.html')

    # Get number of total questions
    total_qty = int(request.POST['qty'])

    # Iteratively count number of correct answers
    correct_qty = 0  # Initialize incorrect answers as 0
    for i in range(total_qty):
        this_q_text = request.POST['question-' + str(i)]
        try:
            this_q = Question.objects.get(question=this_q_text)
            this_ans = request.POST['answer-' + str(i)]
            this_type = request.POST['q-type-' + str(i)]
            is_correct = False  # Initialize answer truthiness as false

            # MultipleChoice
            if this_type == MULTIPLE_CHOICE:
                is_correct = MultipleChoice.custom.is_correct(question=this_q, answer=this_ans)
            # TrueFalse
            else:
                is_correct = TrueFalse.custom.is_correct(question=this_q, answer=this_ans)

            # Answer correct - increment correct qty
            if is_correct:
                correct_qty += 1
            # Answer incorrect - don't increment
            else:
                pass
        # Answer not selected
        except MultiValueDictKeyError:
            pass

    # Get game id for user and record results
    try:
        game_pk = request.POST['game-id']
        # Score.custom.end
    except:
        # User's game was not recorded
        error_msg = "No valid game id - score not recorded"


    # Map variables for template to use
    context = {
        'total': total_qty,
        'correct': correct_qty
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


