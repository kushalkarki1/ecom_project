from django.contrib import admin
from product.models import Category, Brand, Tag, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at", )
    search_fields = ("name", )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "marked_price", "discount", "display_price", )
    search_fields = ("name", "sku",)
    list_filter = ("status", )