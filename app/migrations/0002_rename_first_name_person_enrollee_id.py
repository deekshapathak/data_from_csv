# Generated by Django 4.1.13 on 2024-09-30 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='enrollee_id',
        ),
    ]
