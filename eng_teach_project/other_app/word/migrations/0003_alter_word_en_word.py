# Generated by Django 4.0.3 on 2022-03-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_alter_word_en_options_alter_word_en_lvl_know_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word_en',
            name='word',
            field=models.SlugField(max_length=25, unique=True, verbose_name='слово'),
        ),
    ]