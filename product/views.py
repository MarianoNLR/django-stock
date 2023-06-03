from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category
from django.core import serializers
from .forms import FilteredSearch


# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all().values()
    if request.method == 'GET' or (request.POST['category'] == "" and request.POST['product_name'] == ""):
        products_json = serializers.serialize("json", products)
        form = FilteredSearch
        #product_list = json.dumps(list(products), cls=DecimalEncoder)
        #category_list = list(categories)
        return render(request, 'home.html', {
            'products': products,
            'form': form,
            'categories': categories
        })
    else:
        # if request.POST['category'] == "" and request.POST['product_name'] == "":
        #     return render(request, 'home.html', {
        #     'products': products,
        #     'form': form,
        #     'categories': categories
        # })
        if request.POST['category'] != "":
            products = products.filter(category_id = request.POST['category'])
        if request.POST['product_name'] != "":
            products = products.filter(name__contains = request.POST['product_name'])
        print(products.exists())
        form = FilteredSearch
        return render(request, 'search-results.html', {
            'products': products,
            'form': form,
            'categories': categories
        })