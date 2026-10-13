from django.contrib import admin
from .models import Comment, CustomUser, Category, Product, ProductImage
# Register your models here.

class ProductImageInline(admin.TabularInline):  # Mahsulot rasmlarini admin panelida ko'rsatish uchun inline klass
    model = ProductImage  # Mahsulot rasmlari modeli

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date_created', 'category', 'author',)  # Admin panelida ko'rsatiladigan ustunlar
    inlines = [ProductImageInline]  # Mahsulot rasmlarini ko'rsatish uchun inline klass

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)                                  # Admin panelida Product modelini ro'yxatga olish va ProductAdmin klassini ishlatish
admin.site.register(ProductImage)
