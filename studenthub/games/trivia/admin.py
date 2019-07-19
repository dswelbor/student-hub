from django.contrib import admin
from .models import Difficulty, Category, Question, MultipleChoice, TrueFalse, Score

"""Adds trivia questions to admin"""
admin.site.register(Question)
admin.site.register(MultipleChoice)
admin.site.register(TrueFalse)
admin.site.register(Difficulty)
admin.site.register(Category)
admin.site.register(Score)
