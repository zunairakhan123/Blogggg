from django.contrib import admin
from .models import Blogs,Category

# Register your models here.
admin.site.register(Category)
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","created_at","author","category","tags","image"]

