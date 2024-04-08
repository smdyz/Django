from django.urls import path

from catalog.views import register
from catalog.views import index
from catalog.views import admin1
from catalog.views import contact
from catalog.views import product
from catalog.apps import MainAppConfig

app_name = MainAppConfig.name

urlpatterns = [
    path('', register, name='register'),
    path('store/', index, name='store'),
    path('admin1/', admin1, name='admin1'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', product, name='product'),
]
