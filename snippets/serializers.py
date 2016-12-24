from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

# Hyperlinking the API, django-rest-framework tutorial part 5
class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'text', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
