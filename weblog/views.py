from django.shortcuts import render
from weblog.models import Product

def weblog_home_views (request):
    products = Product.objects.all()
    context = dict (
        products=products,
    )
    return render (request, "main_pages/weblog-home.html", context)


