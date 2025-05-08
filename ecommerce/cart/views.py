from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1  # If item already exists, increase quantity
    cart_item.save()
     
    print("Added to Cart:", cart_item)
    return redirect('view_cart')


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    print("Cart Items:", cart_items)  # Debugging: Check if items exist
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})


@login_required
def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)  # Ensure user match
    cart_item.delete()
    return redirect('view_cart')
    
def update_cart(request, product_id):
    """Update the quantity of a product in the cart"""
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "increase":
            cart_item.quantity += 1  # Increase quantity
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1  # Decrease quantity
        cart_item.save()

    return redirect("view_cart")  # Redirect to cart page