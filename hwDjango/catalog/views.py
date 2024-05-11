from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, UserForm, VersionForm
from .models import Product, Users, Version

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

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['Version'] = Version.objects.filter(sign=True)
        # print(context)
        return context


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/blog_form.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')


class UserCreateView(CreateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('catalog:store')


class UserUpdateView(UpdateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('catalog:store')


class VersionListView(ListView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product/<int:pk>')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:store')


class VersionDetailView(DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for data in context_data:
            if data['sign'] is True:
                return context_data


class VersionDeleteView(DeleteView):
    pass


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
