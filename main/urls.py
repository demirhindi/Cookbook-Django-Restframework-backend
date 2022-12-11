from django.urls import path,include

from main import views
from rest_framework import routers
from .views import CreateMealViewSet,CreateRecipeViewSet
router = routers.DefaultRouter()
router.register('createmeal', CreateMealViewSet)
router.register('createrecipe', CreateRecipeViewSet)

urlpatterns = [
    path('example/', views.get_example),
    path('categories/', views.get_categories),
    path('category/<slug:category_slug>/', views.get_category),
    
    path('meals/<slug:category_slug>/', views.get_meals), 
    path('meal/addmeal/', views.add_meal), 
    path('meal/deletemeal/', views.delete_meal), 

    path('', include(router.urls)),

    path('recipes/<slug:meal_slug>/', views.get_recipes),    
    path('recipe/<slug:recipe_slug>/', views.get_recipe),  
    path('recip/addrecipe/', views.add_recipe),
    path('recip/deleterecipe/', views.delete_recipe),



    path('recipes/<slug:recipe_slug>/newcomment/', views.add_comment),
    path('recipes/<slug:recipe_slug>/allcomments/', views.get_comments),  

    path('search/', views.RecipeSearchListView.as_view()),


    
    
]