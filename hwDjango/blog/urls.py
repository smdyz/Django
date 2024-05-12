from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogConfig.name


urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='create'),
    path('blog_list/', BlogListView.as_view(), name='list'),
    path('blog_details/<int:pk>', BlogDetailView.as_view(), name='details'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]
