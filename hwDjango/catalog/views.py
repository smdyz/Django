from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, VersionForm
from .models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        active_versions = []
        for prod in context_data.get('object_list'):
            print(context_data)
            active_versions.append(prod.version.filter(sign=True).first())
        context_data['active_versions'] = active_versions
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')
    login_url = '/users/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        print(self.object.author)
        self.object.author.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:store')
    login_url = '/users/'
    redirect_field_name = 'redirect_to'


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
    model = Version
    success_url = reverse_lazy('catalog:store')


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
