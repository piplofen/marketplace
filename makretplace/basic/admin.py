from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "article", "manufacture", "description", "price", "category")
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "article", "manufacture", "category")
    ordering = ["id"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    ordering = ["id"]

class ManufactureAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "address")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    ordering = ["id"]

admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)