from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"
    ordering = ["price_pay"]  # сортирует товары по цене в порядке возрастания
    paginate_by = 10  # на странице показывает товары по 10 штук


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"  # выводит подробную информацию о товаре


class ContactListView(ListView):
    model = Contact
    template_name = "contact_list.html"  # выводит страницу с контактами
    context_object_name = "contacts"  # имя контекстного объекта для шаблона


# class ContactView(TemplateView):
#     template_name = "contact_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["contact"] = Contact.objects.all()
#         return context



# def contacts(request):
#     return render(request, "contact_list.html")
