from django.contrib import admin
from .models import Category  # Импортируйте вашу модель из models.py
from mptt.admin import MPTTModelAdmin

# @admin.register(CategoryAdmin)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('parent', 'name')


# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#

# admin.site.register(Post, PostAdmin)


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)