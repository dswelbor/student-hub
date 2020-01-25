from django.db import models


class FlashcardManager(models.Manager):
    """Custom model manager for custom Flashcard querysets"""
    def get_flashcards(self, qty, subject=None, course=None, module=None):
        """Returns a QuerySet of random questions that meet passed criteria"""

        # Randomly ordered queryset
        flashcards_rng = super(FlashcardManager, self).get_queryset().order_by('?')

        if subject:
            flashcards_rng = flashcards_rng.filter(module__course__subject__subject=subject)

        if course:
            flashcards_rng = flashcards_rng.filter(module__course__course=course)

        if module:
            flashcards_rng = flashcards_rng.filter(module__module=module)

        # Return random flashcards
        return flashcards_rng[:qty]
