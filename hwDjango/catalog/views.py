from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, VersionForm
from .models import Product, Version


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
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['Version'] = Version.objects.filter(sign=True)
        #     context.version = Version.objects.get(product=name)
        # print(context)
        return context


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/blog_form.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')
    login_url = '/users/'
    redirect_field_name = 'redirect_to'  # зачем?

    # def form_valid(self, form):
    #     prod_data = form.save(commit=False)
    #     print(self.request.user)

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         if isinstance(instance, Request):
    #             if not instance.usercreated:
    #                 instance.usercreated = request.user
    #             instance.save()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')
    login_url = '/users/'
    redirect_field_name = 'redirect_to'  # зачем?


class VersionListView(ListView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:store')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:store')


class VersionDetailView(DetailView):
    model = Version


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
