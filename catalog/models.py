from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Укажите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Опишите категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Укажите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Опишите продукт",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='category'
    )
    price_pay = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Цена за покупку",
        help_text="Введите цену"
    )
    created_at = models.DateTimeField(verbose_name="Дата создания записи", help_text="Введите дату")
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения записи",
        help_text="Введите дату"
    )
    manufactured_at = models.DateTimeField(
        verbose_name="Дата производства продукта",
        help_text="Введите дату",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price_pay"]

    def __str__(self):
        return f'{self.name}, {self.category}'

