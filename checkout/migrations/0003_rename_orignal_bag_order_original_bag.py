# Generated by Django 3.2.15 on 2022-10-15 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20221015_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orignal_bag',
            new_name='original_bag',
        ),
    ]
