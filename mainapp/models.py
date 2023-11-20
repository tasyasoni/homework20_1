from django.conf import settings
from django.db import models, connection

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')


    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE mainapp_category RESTART IDENTITY CASCADE')



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', unique=True, **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='описание')
    picture = models.ImageField(upload_to = 'mainapp', verbose_name='картинка', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='цена')
    data_life = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_chadge = models.DateField(**NULLABLE, verbose_name='дата_изменения')
    owner = models.ForeignKey('usersapp.User', on_delete=models.SET_NULL, verbose_name='id_пользователя', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак_публикации')


    def __str__(self):
        return  f'{self.name}'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='id_product')
    number_version = models.IntegerField(verbose_name='номер_версии')
    name = models.CharField(max_length=100, verbose_name='наименование')
    current_version = models.BooleanField(verbose_name='признак_текущей_версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

