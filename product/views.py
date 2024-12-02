from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def home( request):
    product = Product.objects.all()
    data = {
        'p' : product
    }
    return render (request, 'product/index.html' , data)
