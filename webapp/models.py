from django.db import models

# Create your models here
class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Вопрос')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.question}'


    class Meta:
        db_table = "Poll"
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Choice(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE,
                                verbose_name='Опрос')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        db_table = "Choice"
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answers', on_delete=models.CASCADE,
                                verbose_name='Опрос')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    choice = models.ForeignKey('webapp.Choice',related_name='answers',on_delete=models.CASCADE,
                               verbose_name='Вариант ответа')

    def __str__(self):
        return f'{self.poll}'

    class Meta:
        db_table = "Answer"
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


