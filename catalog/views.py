from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from catalog.models import Product, Contact, Blog
from pytils.translit import slugify


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
    success_url = reverse_lazy("catalog:contact_list")  # переходит на страницу


# class ContactView(TemplateView):
#     template_name = "contact_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["contact"] = Contact.objects.all()
#         return context


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])