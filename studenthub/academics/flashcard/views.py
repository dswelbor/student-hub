from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import Subject, Course, Module, FlashcardTag, Flashcard, FlashcardStat
from django.contrib.auth.decorators import login_required  # Require users to be logged in to access page

SELECT = '--Select--'


@login_required
def index(request):
    """Simple initial index view for flashcard app"""

    # Dynamically get data for difficulties and categories
    subject_list = Subject.objects.all().order_by('subject')
    course_list = Course.objects.all().order_by('course')
    module_list = Module.objects.all().order_by('module')
    template = loader.get_template('flashcard/index.html')

    # Map variables for template to use
    context = {
        'SELECT': '--Select--',
        'subject_list': subject_list,
        'course_list': course_list,
        'module_list': module_list
    }
    return HttpResponse(template.render(context, request))


@ login_required
def study(request):
    """This view delivers random flashcards based on selection criteria"""
    # html template for view
    template = loader.get_template('flashcard/study.html')

    try:
        # flashcard params
        subject = request.POST['subject-questions']
        course = request.POST['course-questions']
        module = request.POST['module-questions']
        qty = int(request.POST['qty-questions'])

    except KeyError:
        # TODO: implement redirect
        # redirect to flashcard/index with message
        pass

    # handle select text
    if subject == SELECT:
        subject = None

    if course == SELECT:
        course = None

    if module == SELECT:
        module = None
    # get random flashcards
    flashcards = Flashcard.custom.get_flashcards(qty, subject=subject, course=course, module=module)

    # Error - no questions
    error_msg = None
    try:
        qty = len(flashcards)
    except TypeError:
        # TODO: Implement error message and redirect to category choice
        error_msg = 'No flashcards found. Please select different subject, course, and module options.'
        qty = 0

    # get list flashcards as json
    flashcards_json = serializers.serialize('json', flashcards)

    # Map variables for template to use
    context = {
        # pass flashcard params
        'subject': request.POST['subject-questions'],
        'course': request.POST['course-questions'],
        'module': request.POST['module-questions'],

        'qty': qty,  # Accommodate less question in pool than passed qty
        'flashcards_json': flashcards_json,
        'error': error_msg
    }

    return HttpResponse(template.render(context, request))
