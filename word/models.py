from django.db import models
from django.urls import reverse


class Word_en(models.Model):
    word = models.SlugField(unique=True, max_length=25, verbose_name='слово')
    translation = models.CharField(max_length=100, verbose_name='перевод')
    lvl_know = models.SmallIntegerField(default=0, verbose_name='уровень знания слова')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
        ordering = ['word']

    def get_absolute_url(self):
        return reverse('run', kwargs={'pk': self.pk})

