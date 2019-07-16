from django.db import models
from config.settings import AUTH_USER_MODEL


class Difficulty(models.Model):
    """
    Simple Schema to outline established difficulty levels
    """
    # Enumerated
    difficulty = models.CharField(max_length=32, primary_key=True)


class Category(models.Model):
    """
    Simple schema that outlines categories for Questions.
    """
    # Enumerated
    category = models.CharField(max_length=64, primary_key=True)


class Question(models.Model):
    """
    Defines the field values for Trivia questions
    """
    # Primary key
    question = models.CharField(max_length=280, primary_key=True)

    # Attributes
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)


class MultipleChoice(models.Model):
    """
    Schema for answers to multiple choice questions
    """
    # Primary key
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)

    # Attributes
    correct_answer = models.CharField(max_length=64)
    incorrect_b = models.CharField(max_length=64)
    incorrect_c = models.CharField(max_length=64)
    incorrect_d = models.CharField(max_length=64)


class TrueFalse(models.Model):
    """
    Schema for answers to T/F trivia questions
    """
    # Primary key
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)

    # Attribute
    correct_answer = models.BooleanField()


class Scores(models.Model):
    """
    Schema for Trivia game scores
    """
    # Auto-gen ID field is game instance primary key

    # Attributes
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    # Entry should be created when game is started
    datetime_start = models.DateTimeField(auto_now_add=True)
    # Entry should be updated when game completes
    datetime_end = models.DateTimeField(blank=True, null=True)
    questions_correct = models.IntegerField()
    total_questions = models.IntegerField()

