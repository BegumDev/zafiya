# Generated by Django 3.2.15 on 2022-10-22 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_postcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment_content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='postcomment',
            old_name='blog',
            new_name='post',
        ),
    ]
