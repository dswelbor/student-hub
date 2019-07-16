# Generated by Django 2.2.3 on 2019-07-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubuser',
            name='alias',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hubuser',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]