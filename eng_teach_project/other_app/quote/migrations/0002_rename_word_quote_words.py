# Generated by Django 4.0.3 on 2022-03-26 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='word',
            new_name='words',
        ),
    ]