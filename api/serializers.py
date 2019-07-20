from rest_framework import serializers
from .models import Favourite, Category, MetaData


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('id', 'title', 'description', 'ranking', 'created_date',
                  'modified_date', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'count')


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'count', 'favourites')


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = ('id', 'name', 'data_type', 'value', 'favourite')
