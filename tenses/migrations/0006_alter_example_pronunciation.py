# Generated by Django 4.0.3 on 2022-03-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenses', '0005_example_pronunciation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='pronunciation',
            field=models.FileField(null=True, upload_to='audio/examples/%Y/%m/%d/'),
        ),
    ]