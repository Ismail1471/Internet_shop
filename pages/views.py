from django.shortcuts import render, HttpResponse
from .models import Category, MainCategory, Product
from django.core.paginator import Paginator

def home_view(request):
    return render(request, "pages/index.html")


def shop_view(request):
    categories = Category.objects.all()
    main_categories = MainCategory.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    number = request.GET.get('page')
    page_obj = paginator.get_page(number)
    context = {
        "categories": categories,
        "main_categories": main_categories,
        "products": page_obj,

    }

    return render(request, "pages/shop.html", context)

def category_products(request, slug):
    main_categories = MainCategory.objects.all()
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    
    context = {
        "main_categories": main_categories,
        "categories": categories,
        "products": products,
    }
    return render(request, "pages/shop.html", context)

def product_detail(request, slug):
    products = Product.objects.get(slug=slug)
    images = products.productimage_set.all()
    context = {
        "product": products,
        "images": images
    }
    return render(request, "pages/product_detail.html", context)



