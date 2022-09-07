from django.shortcuts import redirect, render
from categories.models import Category
from categories.forms import CategoryForm

# Create your views here.
def list_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'categories/list_categories.html', context=context)

def all_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'categories/all_categories.html', context=context)

def create_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                keywords = form.cleaned_data['keywords']
            )

            return redirect(list_categories)

    elif request.method == 'GET':
        form = CategoryForm()
        context = {'form': form}

        return render(request, 'categories/create_category.html', context=context)

def update_category(request, pk):
    
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = Category.objects.get(id=pk)
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            category.keywords = form.cleaned_data['keywords']
            category.is_active = form.cleaned_data['is_active']

            category.save()
            return redirect(list_categories)

    elif request.method == "GET":
        category = Category.objects.get(id=pk)

        form = CategoryForm(
            initial={
                'name': category.name,
                'description': category.description,
                'keywords': category.keywords,
                'is_active': category.is_active
            }
        )

        context = {'form': form}

        return render(request, 'categories/update_category.html', context=context)
