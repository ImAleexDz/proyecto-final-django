from email.mime import image
from math import prod
from typing import List
from unicodedata import name
from django.shortcuts import redirect, render
from productos.models import Products
from .forms import ProductForm
from categories.models import Category
import json

def create_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                category = form.cleaned_data['category'],
                image = form.cleaned_data['image']
            )

        return redirect(all_products)

    elif request.method == "GET":
        form = ProductForm()
        context = {'form': form}
    
        return render(request, "products/new_product.html", context=context)

def list_products(request):

    products = Products.objects.all()
    categories = Category.objects.all()
        
    context = {
        "products": products,
        "categories": categories
        }
    return render(request, "products/list_products.html", context=context)

def all_products(request):
    products = Products.objects.all()
        
    context = {
        "products": products
        }

    return render(request, "products/all_products.html", context=context)


def view_product(request, pk):

    product = Products.objects.get(id=pk)

    context={'product': product}

    return render(request, "products/view_product.html", context=context)

def update_product(request, pk):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = Products.objects.get(id=pk)

            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.is_active = form.cleaned_data['is_active']
            product.category = str(form.cleaned_data['category'])

            product.save()

            return redirect(all_products)

    elif request.method == "GET":
        product = Products.objects.get(id=pk)

        form = ProductForm(
            initial={
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'is_active': product.is_active,
                'category': product.category
            }
        )
        context = {'form': form}

        return render(request, 'products/update_product.html', context=context)

def delete_product(request, pk):
    if request.method == "GET":
        product = Products.objects.get(id=pk)
        context = {"product": product}

        return render(request, 'products/delete_product.html', context=context)

    elif request.method == "POST":
        product = Products.objects.get(id=pk)
        product.delete()

        return redirect(all_products)
