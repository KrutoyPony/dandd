from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL (slug)")
    image = models.ImageField(upload_to="categories/", blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название товара")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (slug)")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Главное изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(default=1, verbose_name="Остаток")
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def __str__(self):
        return self.name