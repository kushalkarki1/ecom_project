from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from shopping.models import Cart, CartItem
from django.views.generic import ListView
from product.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect


class CartListView(ListView):
    model = Cart
    template_name = "list_cart.html"
    context_object_name = "carts"


def add_to_cart(request):
    # product should be added to cart
    # cart item should be created and added to cart
    # which has not been checked out yet
    obj, created = Cart.objects.get_or_create(
        is_checked_out=False,
        defaults={
            "is_checked_out": False
        }
    )
    productid=request.POST.get("productid")
    product = get_object_or_404(Product, id=productid)
    CartItem.objects.create(
        product=product,
        unit_price=product.display_price,
        cart=obj
    )
    messages.add_message(request, messages.INFO, "Product added to cart successfully.")
    return HttpResponseRedirect(reverse("product:product_detail", args=(productid,)))
