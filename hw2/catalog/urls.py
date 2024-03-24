from django.urls import path

from catalog.views import register
from catalog.views import index
from catalog.views import admin1
from catalog.views import contact

urlpatterns = [
    path('', register),
    path('store', index),
    path('admin1', admin1),
    path('contact', contact),
]
