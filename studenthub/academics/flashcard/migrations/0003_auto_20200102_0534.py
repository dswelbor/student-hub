# Generated by Django 2.2.3 on 2020-01-02 05:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcard', '0002_auto_20191223_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FlashcardStats',
            new_name='FlashcardStat',
        ),
    ]
