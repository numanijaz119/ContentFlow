from django.contrib import admin
from .models import Post, Comment, Topic, Category, Media, SEO

# Register your models here, 
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(SEO)