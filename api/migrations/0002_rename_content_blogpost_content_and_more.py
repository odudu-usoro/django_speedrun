# Generated by Django 5.2 on 2025-04-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='Time_created',
            new_name='time_created',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='Title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
