from django.shortcuts import render, redirect

from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeView(request):

    search = request.GET.get('search')

    if (search):
        products = Product.objects.filter(name__icontains=search)

    else: 
        products = Product.objects.all().order_by('-created_at')

    return render(request, "home.html", {"products" : products});


@login_required
def DashboardView(request):

    products = Product.objects.all().order_by('-created_at')

    return render(request, 'dashboard.html', {'products': products})

