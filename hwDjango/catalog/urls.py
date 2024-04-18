from django.urls import path

from catalog.views import ProductListView, register, admin1, contact, ProductDetailView
from catalog.apps import MainAppConfig

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = MainAppConfig.name
app_name = BlogConfig.name

urlpatterns = [
    path('', register, name='register'),
    path('store/', ProductListView.as_view(), name='store'),
    path('admin1/', admin1, name='admin1'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_details/<int:pk>', ProductDetailView.as_view(), name='blog_details'),
    path('blog_create/<int:pk>', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
