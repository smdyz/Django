from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


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


def product(request):
    return render(request, 'catalog/product.html')
