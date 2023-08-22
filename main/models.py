from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} - {self.category} - {self.price} - {self.create_date} - {self.date_update}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
