from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import Subject, Course, Module, FlashcardTag, Flashcard, FlashcardStats
from django.contrib.auth.decorators import login_required  # Require users to be logged in to access page


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
