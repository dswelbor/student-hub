from django.db import models
from config.settings import AUTH_USER_MODEL


class Difficulty(models.Model):
    """
    Simple Schema to outline established difficulty levels
    """
    # Enumerated
    difficulty = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.difficulty


class Category(models.Model):
    """
    Simple schema that outlines categories for Questions.
    """
    # Enumerated
    category = models.CharField(max_length=140, primary_key=True)

    def __str__(self):
        return self.category


class Question(models.Model):
    """
    Defines the field values for Trivia questions
    """
    # Primary key
    question = models.CharField(max_length=280, primary_key=True)

    # Attributes
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a String representation of a Question object"""
        return "{} | {} | {}".format(self.question, self.category, self.difficulty)


class MultipleChoice(models.Model):
    """
    Schema for answers to multiple choice questions
    """
    # Primary key
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)

    # Attributes
    correct_answer = models.CharField(max_length=140)
    incorrect_b = models.CharField(max_length=140)
    incorrect_c = models.CharField(max_length=140)
    incorrect_d = models.CharField(max_length=140)

    def __str__(self):
        """Returns a String representation of the MC question"""
        return "{} | ans: {} | incorrect: {}, {}, {}".format(self.question, self.correct_answer, self.incorrect_b,
                                                             self.incorrect_c, self.incorrect_d)


class TrueFalse(models.Model):
    """
    Schema for answers to T/F trivia questions
    """
    # Primary key
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)

    # Attribute
    correct_answer = models.BooleanField()

    def __str__(self):
        """Returns a String representation of the T/F question"""
        return "{} ans: {}".format(self.question, self.correct_answer)


class Score(models.Model):
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
    questions_correct = models.IntegerField(blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """Returns a String Representation of a trivia game score"""
        return "{} | {} | start: {} end: {} | pts: {} out of: {}".format(self.username, self.difficulty,
                                                                         self.datetime_start, self.datetime_end,
                                                                         self.questions_correct, self.total_questions)
