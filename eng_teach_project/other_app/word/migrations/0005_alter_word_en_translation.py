# Generated by Django 4.0.3 on 2022-03-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0004_alter_word_en_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word_en',
            name='translation',
            field=models.CharField(max_length=100, verbose_name='перевод'),
        ),
    ]
