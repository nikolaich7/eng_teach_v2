from django.db import models
from word.models import Word_en

class Quote(models.Model):
    quote = models.CharField(max_length=250, verbose_name='цитата')
    translation = models.CharField(max_length=250, verbose_name='перевод')
    words = models.ManyToManyField(Word_en, verbose_name='связанные слова')

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'цитата'
        verbose_name_plural = 'цитаты'
        ordering = ['-id']