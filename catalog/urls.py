from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('contacts/', contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


