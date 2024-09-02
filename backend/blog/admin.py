from django.contrib import admin
from .models import Post, Comment, Tag, Category

# Register your models here
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)