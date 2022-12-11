from django.shortcuts import render

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Example,Category,Meals,Recipe,Comment
from .serializers import ExampleSerializer,CategorySerializer,MealsSerializer,RecipeSerializer,CommentsSerializer,MealsEntrySerializer, RecipeEntrySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class RecipeSearchListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['title','meterials']

   

@api_view(['GET'])
def get_example(request):
    myexample = Example.objects.all()
    serializer = ExampleSerializer(myexample, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_category(request,category_slug):
    try:
        queryset = Category.objects.get(slug=category_slug)

    except Category.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)



@api_view(['GET'])
def get_meals(request,category_slug):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    
    try:
        detail = get_object_or_404(Category, slug=category_slug)
        queryset = Meals.objects.filter(categories=detail).order_by('id') 

    except Meals.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = MealsSerializer(queryset, many=True)
        return Response(serializer.data)   





@api_view(['GET'])
def get_recipes(request, meal_slug):
    try:
        detail = get_object_or_404(Meals, slug=meal_slug)
        queryset = Recipe.objects.filter(meals=detail).order_by('id') 

    except Recipe.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        recipe_serializer = RecipeSerializer(queryset, many=True)
        data = {
        'recipe': recipe_serializer.data,
        
        }
        return Response(data)


@api_view(['GET'])
def get_recipe(request,recipe_slug):
    try:
        queryset = Recipe.objects.get(slug=recipe_slug)

    except Category.DoesNotExist:
        return Response(
            {
              'errors':{'code':404, 'message':'Böyle bir çalışma bulunamadı.'}
                },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        recipe_serializer = RecipeSerializer(queryset)
        data = {
        'recipe': recipe_serializer.data,
        
        }
        return Response(data)


@api_view(['GET'])
def get_comments(request, recipe_slug):
    queryset = Recipe.objects.get(slug=recipe_slug)
    serializer = CommentsSerializer(queryset.comments.all(), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request, recipe_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    queryset = Recipe.objects.get(slug=recipe_slug)
    

    comment = Comment.objects.create(recipe=queryset, name=name, content=content, created_by=request.user)

    return Response({'message': 'The comment was added!'})





    

@api_view(['POST'])
def add_meal(request):
    data = request.data   
    category_slug=data.get('categoryName')
    meals_slug=data.get('mealName')
    querysetCategory = Category.objects.get(slug=category_slug)
    querysetMeals = Meals.objects.get(slug=meals_slug)    
    querysetMeals.categories.add(querysetCategory)
    return Response({'message': 'The meal is added!'})


@api_view(['POST'])
def delete_meal(request):
    data = request.data   
    meals_slug=data.get('mealName')   
    querysetMeals = Meals.objects.get(slug=meals_slug)
    querysetMeals.delete()   
    return Response({'message': 'The meal is deleted!'})

@api_view(['POST'])
def delete_recipe(request):
    data = request.data   
    recipe_slug=data.get('recipeName')   
    querysetRecipe = Recipe.objects.get(slug=recipe_slug)
    querysetRecipe.delete()   
    return Response({'message': 'The meal is deleted!'})




@api_view(['POST'])
def add_recipe(request):
    data = request.data    
    meals_slug=data.get('mealName')
    recipe_slug=data.get('recipeName')
    querysetMeals = Meals.objects.get(slug=meals_slug)
    querysetRecipe = Recipe.objects.get(slug=recipe_slug)    
    querysetRecipe.meals.add(querysetMeals)
    return Response({'message': 'The meal is added!'})




class CreateMealViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsEntrySerializer

    def post(self, request, *args, **kwargs):
        image = request.data['image']
        title1 = request.data['title']
        meals=Meals.objects.create(title=title1, image=image)        
        return Response({'message': 'Meal created'})

class CreateRecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeEntrySerializer

    def post(self, request, *args, **kwargs):
        image = request.data['image']
        title1 = request.data['title']
        longDesc = request.data['longDesc']
        meterials = request.data['meterials']      

        meals=Recipe.objects.create(title=title1, image=image, longDesc=longDesc, meterials=meterials)
        
        return Response({'message': 'Recipe created'})




    


    