from django.urls import path
from shopping.views import CartListView, add_to_cart, remove_cart_item

app_name = "shopping"

urlpatterns = [
    path("mycart/", CartListView.as_view(), name="mycart"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("remove-cart-item/", remove_cart_item, name="remove_cart_item"),
]