from django.contrib import admin

from catalog.models import Category, Product, Contact


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_pay", "category")
    list_filter = ("category", )
    search_fields = ("name", "description",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "contact", "email", "inn", "ogrn")
