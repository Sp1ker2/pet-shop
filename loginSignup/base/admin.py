
# Register your models here.
from django.contrib import admin
from .models import Category
from .models import Product

admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}

from .models import Order

admin.site.register(Order)
