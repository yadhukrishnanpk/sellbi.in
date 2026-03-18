from django import template

register = template.Library()

@register.simple_tag(name='gettotal')
def gettotal(cart):
    total = 0
    if cart:
        for item in cart.added_Items.all(): 
            if item.product and item.product.price:
                total += item.quantity * item.product.price
    return total