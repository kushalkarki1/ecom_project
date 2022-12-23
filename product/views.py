from django.shortcuts import render
from product.models import Product, Status, Category


def get_all_categories():
    return Category.objects.all()


def home(request):
    categories = get_all_categories()
    context = {"categories": categories}
    return render(request, "home.html", context)


def product_list_view(request):
    products = Product.objects.filter(status=Status.PUBLISH)
    categories = get_all_categories()
    context = {"categories": categories, "products": products}
    return render(request, "product_list.html", context)


def product_detail_view(request, productid):
    product = Product.objects.get(id=productid)
    categories = get_all_categories()
    context = {"product": product, "categories": categories}
    return render(request, "product_detail.html", context)


def product_by_category_view(request, categoryid):
    category = Category.objects.get(id=categoryid)
    products = category.product_set.filter(status=Status.PUBLISH)
    context = {
        "category": category,
        "products": products,
        "categories": get_all_categories()
    }
    return render(request, "product_list_by_category.html", context)


def product_add_view(request):
    return render(request, "product_add.html")