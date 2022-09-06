from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=40, required=True)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 20,}), label="Descripción")
    keywords = forms.CharField(label="Palabras Clave", required=False)
    is_active = forms.BooleanField(label="Activo?", required=True)