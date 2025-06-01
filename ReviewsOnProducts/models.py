from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва продукту")
    description = models.TextField(verbose_name="Опис продукту")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Продукт")
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст відгуку")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Рейтинг") # Рейтинг від 1 до 5

    def __str__(self):
        return f'Відгук від {self.author} для {self.product.name}'