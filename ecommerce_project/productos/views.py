from unicodedata import name
from django.shortcuts import redirect, render
from productos.models import Products
from .forms import ProductForm

def create_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                is_active = form.cleaned_data['is_active'],
                category = form.cleaned_data['category']
            )

        return redirect(list_products)

    elif request.method == "GET":
        form = ProductForm()
        context = {'form': form}
    
        return render(request, "new_product.html", context=context)

def list_products(request):

    products = Products.objects.all()

    context = {
        "products": products
    }

    return render(request, "products/list_products.html", context=context)

def view_product(request, pk):

    product = Products.objects.get(id=pk)

    context={'product': product}

    return render(request, "products/view_product.html", context=context)