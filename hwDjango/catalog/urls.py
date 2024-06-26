from django.urls import path

from catalog.views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView, ProductListView, ProductDeleteView, admin1, contact, ProductDetailView, ProductCreateView, ProductUpdateView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView, VersionDeleteView
from catalog.apps import MainAppConfig
from django.views.decorators.cache import cache_page


app_name = MainAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='store'),
    path('admin1/', admin1, name='admin1'),
    path('contact/', contact, name='contact'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/versions/', VersionListView.as_view(), name='product_versions'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('version_update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
    path('version_delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
]
