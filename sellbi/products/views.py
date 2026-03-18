from django.shortcuts import render, get_object_or_404
from .models import Product


def product(request):
    
    products = Product.objects.filter(delete_status=1)
    context = {'products': products}
    return render(request, "products.html", context)


def productdetails(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_details.html",{'product': product}) 