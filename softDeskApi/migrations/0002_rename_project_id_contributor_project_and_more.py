# Generated by Django 4.0 on 2021-12-20 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softDeskApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='assignee_user_id',
            new_name='assignee_user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='author_user_id',
            new_name='author_user',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='author_user_id',
            new_name='author_user',
        ),
    ]