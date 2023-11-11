from django.db import models
from constants import NULLABLE


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Item name'),
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Original price'),
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Final price', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.final_price}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
