from django.contrib import admin

from .models import Product, Category


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
