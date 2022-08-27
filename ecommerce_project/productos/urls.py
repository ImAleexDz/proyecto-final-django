from unicodedata import name
from django.urls import path
from productos.views import create_product, list_products

urlpatterns = [
    path('create-product/', create_product, name="create-product"),
    path('list-products/', list_products, name="list-products")
]