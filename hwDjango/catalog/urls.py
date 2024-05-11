from django.urls import path

from catalog.views import UserCreateView, UserUpdateView, ProductListView, admin1, contact, ProductDetailView, ProductCreateView, ProductUpdateView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView
from catalog.apps import MainAppConfig


app_name = MainAppConfig.name

urlpatterns = [
    path('', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('store/', ProductListView.as_view(), name='store'),
    path('admin1/', admin1, name='admin1'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/versions/', VersionListView.as_view(), name='product_versions'),
    path('create_version/', VersionCreateView.as_view(), name='create_version')
]
