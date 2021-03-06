# Generated by Django 4.0.3 on 2022-03-26 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('word', '0002_alter_word_en_options_alter_word_en_lvl_know_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=250, verbose_name='слово')),
                ('translation', models.CharField(max_length=250, verbose_name='перевод')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='word.word_en')),
            ],
            options={
                'verbose_name': 'цитата',
                'verbose_name_plural': 'цитаты',
                'ordering': ['quote'],
            },
        ),
    ]
