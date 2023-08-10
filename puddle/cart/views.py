from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from item.models import Item

@login_required
def add_to_cart(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, _ = CartItem.objects.get_or_create(cart=cart, item=item)
    
    return redirect('cart:index')

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.quantity * item.item.price for item in cart_items)
    
    return render(request, 'cart/index.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
