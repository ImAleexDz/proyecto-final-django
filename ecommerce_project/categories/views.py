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
