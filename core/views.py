from django.shortcuts import render
from products.models import Product

def index(request):
    products = Product.objects.all()[:4]
    return render(request, 'core/index.html', {'products': products})
