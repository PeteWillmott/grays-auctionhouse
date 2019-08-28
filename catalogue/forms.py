from django import forms
from .models import Catalogue

class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = [
            'name',
            'description',
            'price',
            'culture',
            'era',
            'image'
        ]
