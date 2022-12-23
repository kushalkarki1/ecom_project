from django.urls import path
from product.views import (
    home,
    product_detail_view,
    product_list_view,
    product_by_category_view,
    product_add_view,
)

app_name = "product"

urlpatterns = [
    path("", home, name="home"),
    path("product-in-detail/<int:productid>/", product_detail_view, name="product_detail"),
    path("product-list/", product_list_view, name="product_list"),
    path(
        "product-by-category/<int:categoryid>/",
        product_by_category_view,
        name="product_by_category"
    ),
    path(
        "product-add/",
        product_add_view,
        name="product_add"
    ),
]