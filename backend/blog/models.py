from django.db import models
from django.utils.text import slugify

from django.contrib.auth import get_user_model


# Models
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "   Category"
    
    def __str__(self):
        return self.name
    

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name = " Topic"
        verbose_name_plural = " Topics"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category', blank=True)
    topic = models.ManyToManyField('Topic', blank=True)
    
    class Meta:
        verbose_name_plural = "  Posts"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    file = models.FileField(upload_to='files/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    

class SEO(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"SEO for {self.post.title}"