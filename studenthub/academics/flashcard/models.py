from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone
from config.settings import AUTH_USER_MODEL

# TODO: revisit the _str implementation for various models


class Subject(models.Model):
    """
    Simple Schema to outline established Subjects for flashcards
    """
    # Enumerated Subject
    subject = models.CharField(max_length=64, unique=True)
    # Subject description
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.subject


class Course(models.Model):
    """
    Simple Schema to outline established Courses for flashcards
    """
    # Enumerated Course
    course = models.CharField(max_length=64, unique=True)
    # Referential Subject
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # Course description
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.course


class Module(models.Model):
    """
    Simple Schema to model established Course Modules for flashcards. Any one Module can only reference
    one Course, but a Course can be referenced by many Modules. A module has the composite primary
    key (CourseName, ModuleName)
    """
    # TODO: handle module, course composite key unicity in validation
    # Enumerated Course Module
    # Note: unique=True unused as composite keys are not supported by current Django implementation
    module = models.CharField(max_length=64)
    # Referential Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Course description
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.module


class Flashcard(models.Model):
    """
    Simple Schema to model Flashcards
    """
    # Enumerated Course
    question = models.CharField(max_length=1024, unique=True)
    # Flashcard short answer
    answer = models.CharField(max_length=64)
    # Referential Module - gets Course Candidate key from module attributes
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    # Approval - is approved?
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class FlashcardTag(models.Model):
    """
    Simple Schema to associate tags like "machine learning" "JavaFX" with flashcards
    """
    # Referential Flashcard
    flashcard = models.ManyToManyField(Flashcard)
    # Tag - ex "JavaFX" or "unit testing"
    tag = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return self.tag


class FlashcardStats(models.Model):
    """
    Schema to model user-specific Flashcard-specific stats
    """
    # User using Flashcard
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Flashcard used by User
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    # Number of correct attempts using flashcard
    correct = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    # Number of total attempts using flashcard
    attempted = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    # Cumulative time spent on flashcard
    elapsed = models.DurationField(default=timedelta())
    # last attempt datetime
    last_attempt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.flashcard
