from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

CHOICE = [('food', 'Еда'), ('milk', 'Молоко'), ('bred', 'Хлеб')]


# Create your models here
class Product(models.Model):
    name = models.TextField(max_length=20, verbose_name='Имя')
    category = models.TextField(choices=CHOICE)
    description = models.TextField(max_length=2000, verbose_name='Описание', null=True, blank=True)
    img = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Аватар')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "Product"
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='review',
                               verbose_name='Пользователь')
    product = models.ForeignKey('webapp.Product',related_name='review', on_delete=models.CASCADE,
                             verbose_name='Продукт')
    text = models.TextField(max_length=2000,verbose_name='Текст отзыва')
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    mod = models.BooleanField(null=True,blank=True,default=False,verbose_name='Модерирование')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.author}'

    class Meta:
        db_table = "Review"
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


