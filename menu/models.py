from django.db import models
from django.urls import reverse, NoReverseMatch

NULLABLE = {'blank': True, 'null': True}

class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    title = models.CharField(max_length=50, verbose_name='Название')
    url = models.CharField(max_length=50, verbose_name='Ссылка', **NULLABLE)
    named_url = models.CharField(max_length=50, verbose_name='Имя ссылки', **NULLABLE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Родитель', **NULLABLE)

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'menu_item'
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'