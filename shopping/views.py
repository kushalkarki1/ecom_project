from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from shopping.models import Cart, CartItem
from django.views.generic import ListView
from product.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = "list_cart.html"
    context_object_name = "carts"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


@login_required
def add_to_cart(request):
    # product should be added to cart
    # cart item should be created and added to cart
    # which has not been checked out yet
    obj, created = Cart.objects.get_or_create(
        is_checked_out=False,
        owner=request.user,
        defaults={
            "is_checked_out": False,
            "owner": request.user,
        }
    )
    productid=request.POST.get("productid")
    if productid:
        product = get_object_or_404(Product, id=productid)
        cartitem, created = CartItem.objects.get_or_create(
            product=product,
            owner=request.user,
            cart=obj,
            defaults={
                "unit_price": product.display_price,
                "cart": obj
            }
        )
        if not created:
            cartitem.quantity = cartitem.quantity + 1
            cartitem.save()
        messages.add_message(request, messages.INFO, "Product added to cart successfully.")
        return HttpResponseRedirect(reverse("product:product_detail", args=(productid,)))
    return HttpResponseRedirect(reverse("product:product_list"))


@login_required
def remove_cart_item(request):
    cart_item_id = request.POST.get("cartitemid")
    cart = get_object_or_404(CartItem, id=cart_item_id)
    cart.delete()
    messages.add_message(request, messages.INFO, "Item removed successfully")
    return HttpResponseRedirect(reverse("shopping:mycart"))