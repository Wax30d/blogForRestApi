from rest_framework import serializers
from .models import Author, Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    post_list = PostSerializer(read_only=True, many=True, source="post_set")
    class Meta:
        model = Author
        fields = '__all__'