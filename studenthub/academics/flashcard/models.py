from django.db import models


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
    one Course, but a Course can be referenced by many Modules.
    """
    # TODO: handle module, course composite key unicity in validation
    # Enumerated Course Module
    # Note: not unique as composite keys are not supported by current Django implementation
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

    # Course description
    description = models.CharField(max_length=128, blank=True, null=True)

    # TODO: Finish implementing these fields

    def __str__(self):
        return self.question