# cart/views.py
from django.shortcuts import render, redirect
from .models import Cart, CartItem, Product
from .forms import AddToCartForm

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = AddToCartForm(request.POST or None)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart:cart_detail')

    return render(request, 'cart/add_to_cart.html', {'form': form, 'product': product})

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total = cart_items.aggregate(sum('product__price'))['product__price__sum']

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})
