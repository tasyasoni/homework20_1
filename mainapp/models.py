from django.db import models

NULLABLE = {'null':True, 'blank':True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')
    picture = models.ImageField(upload_to = 'mainapp/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    data_life = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_chadge = models.DateField(**NULLABLE, verbose_name= 'дата_изменения')


    def __str__(self):
        return  f'{self.name}, {self.category}'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')


    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'