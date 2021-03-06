# Generated by Django 4.0.3 on 2022-03-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenses', '0003_profile_current_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True, verbose_name='слово')),
                ('translation', models.CharField(max_length=100, verbose_name='перевод')),
            ],
            options={
                'verbose_name': 'слово',
                'verbose_name_plural': 'слова',
                'ordering': ['-id'],
            },
        ),
    ]
