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

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('g', kwargs={'pk': self.pk})