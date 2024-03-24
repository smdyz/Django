from django.shortcuts import render


def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'{email} {password} ')

    return render(request, 'catalog/index.html')
