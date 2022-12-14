from django.shortcuts import render
from categories.models import Category

def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'index.html', context=context)