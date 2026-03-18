from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderedItems
from products.models import Product
from django.contrib import messages

# orders/views.py
@login_required(login_url='login')
def show_cart(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'cart.html', {'cart': None, 'items': []})

    cart_obj = Order.objects.filter(owner=user.customer_profile, order_status=Order.CART_STAGE).first()
    
    items = []
    if cart_obj:
        items = OrderedItems.objects.filter(owner=cart_obj)
    
    return render(request, 'cart.html', {'cart': cart_obj, 'items': items})

@login_required(login_url='login')
def add_to_cart(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile 
        quantity = int(request.POST.get("quantity", 1))
        product_id = request.POST.get("product_id")
        
        product = get_object_or_404(Product, pk=product_id)
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        ordered_item = OrderedItems.objects.filter(
            product=product,
            owner=cart_obj
        ).first()

        if ordered_item:
            ordered_item.quantity += quantity
            ordered_item.save()
        else:
            OrderedItems.objects.create(
                product=product,
                owner=cart_obj,
                quantity=quantity
            )
        return redirect('cart') 
    return redirect('cart')

def remove_item_from_cart(request, pk):
    item = get_object_or_404(OrderedItems, pk=pk)
    
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
        
    return redirect('cart')

@login_required(login_url='login')
def checkout(request):
    user = request.user
    customer = user.customer_profile  
    cart_obj = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
    try:    
        if request.method == "POST":
            Total = float(request.POST.get('total'))
            if cart_obj:
                cart_obj.total_price=Total
                cart_obj.order_status = Order.ORDER_CONFIRMED
                cart_obj.save()
                messages.success(request, "Order confirmed!  We've received your request.   Thank you!!")
                return redirect('cart') 
            else:
                messages.error(request, "SORRY UNABLE TO PROCESS THE ORDER")
    except Exception as e:
        messages.error(request, "SORRY UNABLE TO PROCESS THE ORDER")
    
    return render(request, "checkout.html", {'cart': cart_obj})