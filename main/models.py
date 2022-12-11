from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Example(models.Model):    
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(blank=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(blank=True)    
    created_at = models.DateField(auto_now_add=True)
    image=models.ImageField(blank=True, null=True,upload_to='categories')

    def __str__(self):
        return self.title

class Meals(models.Model):
    categories = models.ManyToManyField(Category,related_name='meals')
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(blank=True)
    image=models.ImageField(upload_to="meals",blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    meals = models.ManyToManyField(Meals, related_name='meals')
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(blank=True)
    image=models.ImageField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    longDesc= models.TextField(max_length=1000000, blank=True)
    meterials=models.TextField(max_length=1000000, blank=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)    
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def pre_save_category(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_category,sender=Category)

def pre_save_meals(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_meals,sender=Meals)

def pre_save_recipe(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_recipe,sender=Recipe)
