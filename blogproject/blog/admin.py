from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

# 为了显示更多的信息
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin) # 把上面注册的PostAdmin也注册进来
admin.site.register(Category)
admin.site.register(Tag)