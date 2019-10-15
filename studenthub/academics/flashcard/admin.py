from django.contrib import admin
from .models import Subject, Course, Module, FlashcardTag, Flashcard, FlashcardStats

"""Adds flashcard models to admin"""
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(FlashcardTag)
admin.site.register(Flashcard)
admin.site.register(FlashcardStats)
