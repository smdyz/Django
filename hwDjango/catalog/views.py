from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


# from django.views.generic.base import TemplateView
#
#
# class ContactPageView(TemplateView):
#     template_name = "contact.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["latest_articles"] = Product.objects.all()
#         return context


class ProductListView(ListView):
    model = Product


# def index(request):
#     prod_list = Product.objects.all()
#     context = {
#         'object_list': prod_list
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/blog_form.html', context)


# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name',)  # 'email', 'password',)
#     success_url = 'catalog:store'

def register(request):
    if request.method == "POST" and request.POST.get('name') == 'admin1' and request.POST.get('password') == 'smidy':
        return render(request, 'catalog/admin1.html')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'{name} {email} {password}')
        return render(request, 'catalog/product_list.html')

    return render(request, 'catalog/product_form.html')


def admin1(request):
    return render(request, 'catalog/admin1.html')


def contact(request):
    return render(request, 'catalog/contact.html')


# class ProductPageView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["latest_articles"] = Product.objects.all()[:5]
#         return context
