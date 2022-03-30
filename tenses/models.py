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
    history = models.JSONField(null=True, verbose_name='история')
    last_example = models.OneToOneField(Example, null=True, verbose_name='последний вопрос', on_delete=models.CASCADE,
                                        related_name='lastexample') # не используется
    last_answer = models.TextField(default='', verbose_name='последний ответ') # не используется
    now_example = models.OneToOneField(Example, null=True, verbose_name='текущий вопроc', on_delete=models.CASCADE,
                                       related_name='noweample') # не используется
    total_answers = models.IntegerField(default=0, verbose_name='ответов всего') # не используется
    right_answers = models.IntegerField(default=0, verbose_name='правильных ответов') # не используется
    wrong_answers = models.IntegerField(default=0, verbose_name='неправильные ответы') # не используется
    current_date = models.CharField(max_length=10, null=True) # не используется

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