from django.contrib import admin

from .models import Product, Category, Users, Version


# admin.site.register(Product) вместо product может быть любая модель (для быстрой регистрации модели)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'category', )
    list_filter = ('name', 'cost', 'category', )
    search_fields = ('name', 'cost', 'category', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', 'email', )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', )
    list_filter = ('version_name', 'version_num', 'product', )
    search_fields = ('version_name', 'version_num', 'product', )
