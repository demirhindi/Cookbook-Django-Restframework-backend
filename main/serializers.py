from rest_framework import serializers

from .models import Example,Category,Comment,Meals,Recipe

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'image')


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('id', 'title', 'slug', 'image')

class MealsEntrySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Meals
        fields = ('id', 'title', 'slug', 'image',)


class RecipeEntrySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Recipe
        fields = ('id', 'title', 'slug', 'image','longDesc','meterials')



class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'slug', 'image','longDesc','meterials')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at')


