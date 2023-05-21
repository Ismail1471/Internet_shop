from django.contrib import admin
from .models import Category, MainCategory, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", 'title', "slug"]
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ["pk", 'title', "slug"]

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", 'title']
    list_display_links = ["pk", 'title']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "quantity", "main_category", "category")
    list_display_links = ("pk", "title")
    list_filter = ("main_category", "category")
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {"slug": ("title",)}