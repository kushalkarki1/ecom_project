from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from product.models import Product, Status, Category
from product.forms import ProductForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages


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
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, "Product added successfully.")
        return HttpResponseRedirect(reverse("product:product_list"))
    return render(request, "product_add.html", {"form": form})


def product_edit_view(request, productid):
    product = get_object_or_404(Product, id=productid)
    # try:
    #     product = Product.objects.get(id=productid)
    # except Product.DoesNotExist:
    #     raise Http404("Product not found")
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, "Product updated successfully.")
        return HttpResponseRedirect(reverse("product:product_list"))
    return render(request, "product_add.html", {"form": form})
