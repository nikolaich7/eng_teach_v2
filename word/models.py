from django.db import models

class Word_en(models.Model):
    word = models.CharField(max_length=25, verbose_name='слово')
    translation = models.TextField(verbose_name='перевод')
    lvl_know = models.SmallIntegerField(default=0, verbose_name='уровень знания слова')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
        ordering = ['lvl_know']

