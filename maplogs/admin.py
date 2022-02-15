from django.contrib import admin
from .models import Map, Category, Product

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'scanned', 'upload_date')
    search_fields = ('title',)
    ordering = ['title']
    filtering = ['scanned']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':  ('name', )}


# Register your models here.
