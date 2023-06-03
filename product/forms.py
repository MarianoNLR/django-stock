from django import forms
from .models import Category
class FilteredSearch(forms.Form):
    product_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Product name', 'class': 'form-group'}))
    category = forms.ModelChoiceField(
        queryset =  Category.objects.all(),
        empty_label="Category",
        required=False,
        widget=forms.Select(attrs={'class': 'form-group'})
    )