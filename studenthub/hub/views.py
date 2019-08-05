from django.http import HttpResponse
from django.template import loader


def index(request):
    """Simple index view for student hub home"""
    template = loader.get_template('hub/index.html')
    # Map variables for template to use
    context = {
        # 'dif_list': difficulty_list,
        # 'cat_list': category_list
    }
    return HttpResponse(template.render(context, request))
