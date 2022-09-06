from unicodedata import name
from django.urls import path
from categories.views import list_categories, create_category, update_category

urlpatterns = [
    path('list-categories/', list_categories, name="list-categories"),
    path('create-categories/', create_category, name="create-categories"),
    path('update-category/<int:pk>/', update_category, name="update-category"),
]