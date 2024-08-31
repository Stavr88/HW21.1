from django.db import models


# Create your models here.
class Contact(models.Model):
    contact = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона контакта",
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        help_text="Укажите адрес электронной почты контакта",
    )
    inn = models.CharField(
        max_length=12,
        verbose_name="ИНН",
        help_text="Укажите ИНН контакта",
    )
    ogrn = models.CharField(
        max_length=15,
        verbose_name="ОГРН",
        help_text="Укажите ОГРН контакта",
    )
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["contact"]

    def __str__(self):
        return self.contact


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
        upload_to="catalog/photo",
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
