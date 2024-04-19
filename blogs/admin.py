from django.contrib import admin
from .models import Category,Blogs,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','author','status','created_at','updated_at','is_featured')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)


admin.site.register(Blogs, BlogsAdmin)

admin.site.register(Comment)

