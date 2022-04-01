from django.contrib.auth.models import User
from django.db import models

class Tense(models.Model):
    tense = models.CharField(unique=True, max_length=30, verbose_name='Время')
    info = models.TextField(verbose_name='Инфо', default='')

    def __str__(self):
        return self.tense

    class Meta:
        verbose_name = 'время'
        verbose_name_plural = 'времена'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('g', kwargs={'pk': self.pk})

class Example(models.Model):
    text = models.TextField(unique=True, max_length=200, verbose_name='Предложение')
    translation = models.TextField(max_length=200, verbose_name='Перевод')
    tense = models.ForeignKey(Tense, on_delete=models.CASCADE)
    pronunciation = models.FileField(upload_to='audio/examples/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('g', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    history = models.JSONField(null=True, verbose_name='история', blank=True)
    history_word = models.JSONField(null=True, verbose_name='история', blank=True)
    history_audio = models.JSONField(null=True, verbose_name='история', blank=True)
    history1 = models.JSONField(null=True, verbose_name='история', blank=True)
    history2 = models.JSONField(null=True, verbose_name='история', blank=True)
    history3 = models.JSONField(null=True, verbose_name='история', blank=True)
    history4 = models.JSONField(null=True, verbose_name='история', blank=True)
    history5 = models.JSONField(null=True, verbose_name='история', blank=True)

    def __str__(self):
        return 'данные ' + self.user.username

    class Meta:
        verbose_name = 'данные пользователя'
        verbose_name_plural = 'данные пользователей'
        ordering = ['-id']


class Word(models.Model):
    word = models.CharField(unique=True, max_length=100, verbose_name='слово')
    translation = models.CharField(max_length=100, verbose_name='перевод')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('run', kwargs={'pk': self.pk})