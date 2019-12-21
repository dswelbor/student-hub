from django.db import models

from django.db.models import Q, F, FloatField, ExpressionWrapper


class FlashcardManager(models.Manager):
    def get_flashcards(self, qty, subject=None, course=None, module=None):
        """Returns a QuerySet of random questions that meet passed criteria"""

        # Randomly ordered queryset
        flashcards_rng = super(FlashcardManager, self).get_queryset().order_by('?')

        #if subject:
        #    flashcards_rng = flashcards_rng.filter(module.course.subject=subject)

        #if course:
        #    flashcards_rng = flashcards_rng.filter(course=course)

        #if module:
        #    flashcards_rng = flashcards_rng.filter(module=module)

        # Return random flashcards
        return flashcards_rng[:qty]
