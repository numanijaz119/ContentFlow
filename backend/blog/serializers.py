from dataclasses import field
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Category, Post, Topic, Comment, Media, SEO


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'media_type', 'description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'slug']

class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = ['title_tag', 'meta_description', 'keywords']
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    # post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    topic = TopicSerializer(many=True)
    media = MediaSerializer(many=True, read_only=True)
    seo = SEOSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'author', 'created_at',
                  'updated_at', 'published_at', 'is_published', 'categories', 'topic',
                  'comments' 'media', 'seo']