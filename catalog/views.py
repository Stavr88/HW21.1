from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Product



class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"
    ordering = ["price_pay"]  # сортирует товары по цене в порядке возрастания
    paginate_by = 10  # на странице показывает товары по 10 штук


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"  # выводит подробную информацию о товаре


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")

    return render(request, 'catalog/contacts.html')
