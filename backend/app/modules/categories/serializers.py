from rest_framework import serializers
from .models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    # author = ProfileSerializer(read_only=True)
    # slug = serializers.SlugField(required=False)
    # hashtagList = HashtagRelatedField(many=True, required=False, source='hashtags')

    class Meta:
        model = Categories
        fields = (
            'id',
            'name',
            'image',
        )
    
    def create(self, validated_data):
        print('************** create category serializer *******************')
        categories = Categories.objects.create(**validated_data)
        return categories
