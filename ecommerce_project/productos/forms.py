from django import forms
from categories.models import Category

    

class ProductForm(forms.Form):

    name = forms.CharField(label="Nombre", max_length=40, required=True)
    price=forms.FloatField(label="Precio", min_value=0.1)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 20,}), label="Descripción")
    is_active= forms.BooleanField(label="Activo?", required=False)
    category= forms.ModelChoiceField(label="Categoría", queryset=Category.objects.all())
    image = forms.ImageField(required=False)
    stock = forms.IntegerField(label="Stock", min_value=0)

