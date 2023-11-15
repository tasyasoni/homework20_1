from django.db import models


NULLABLE = {'null': True, 'blank': True}

class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='слаг')
    blog_content = models.TextField(max_length=500, verbose_name='содержимое')
    picture = models.ImageField(upload_to = 'blogapp', verbose_name='картинка', **NULLABLE)
    data_life = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    public_sign = models.BooleanField(default=True, verbose_name='признак_публикации')
    number_of_views = models.IntegerField (**NULLABLE, verbose_name='количество просмотров')


    def __str__(self):
        return  f'{self.header}'


    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
