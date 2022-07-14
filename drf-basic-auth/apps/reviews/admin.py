from django.contrib import admin
from .models import Product, Category, Comment, Company, ProductSite, ProductSize
from django.contrib.auth.models import Group


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )


# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(ProductSite)
admin.site.register(ProductSize)

admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"
