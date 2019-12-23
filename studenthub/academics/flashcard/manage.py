from django.db import models

from django.db.models import Q, F, FloatField, ExpressionWrapper
# from .models import Subject, Course, Module


class FlashcardManager(models.Manager):
    def get_flashcards(self, qty, subject=None, course=None, module=None):
        """Returns a QuerySet of random questions that meet passed criteria"""

        # Randomly ordered queryset
        flashcards_rng = super(FlashcardManager, self).get_queryset().order_by('?')

        if subject:
            # subjects = Subject.objects.get_queryset().filter(subject=subject)
            flashcards_rng = flashcards_rng.filter(module__course__subject__subject=subject)
        # else:
            # subjects = Subject.objects.get_queryset()

        if course:
            flashcards_rng = flashcards_rng.filter(module__course__course=course)
            # courses = Subject.objects.get_queryset().filter(course=course)
        # else:
            # courses = Subject.objects.get_queryset().filter(course__in=subjects)

        if module:
            flashcards_rng = flashcards_rng.filter(module__module=module)
            # flashcards_rng.filter(module__module=module)
        # else:
            #flashcards_rng.filter(module__in=courses)


        # Return random flashcards
        return flashcards_rng[:qty]
