# Generated by Django 4.0.3 on 2022-03-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_alter_quote_options'),
        ('word', '0007_rename_word_en_worden_alter_worden_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WordEn',
            new_name='Word',
        ),
    ]