from django.contrib import admin
from .models import Category  # Импортируйте вашу модель из models.py


@admin.register(Category)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name')
