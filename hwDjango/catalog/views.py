from django.shortcuts import render
from .models import Product


def index(request):
    prod_list = Product.objects.all()
    context = {
        'object_list': prod_list
    }
    return render(request, 'catalog/index.html', context)


def register(request):
    if request.method == "POST" and request.POST.get('name') == 'admin1' and request.POST.get('password') == 'smidy':
        return render(request, 'catalog/admin1.html')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'{name} {email} {password}')
        return render(request, 'catalog/index.html')

    return render(request, 'catalog/register.html')


def admin1(request):
    return render(request, 'catalog/admin1.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)
