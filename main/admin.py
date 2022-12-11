from django.contrib import admin

from .models import Example,Category,Meals,Recipe,Comment

admin.site.register(Example)
admin.site.register(Category)
admin.site.register(Meals)
admin.site.register(Recipe)
admin.site.register(Comment)

# Register your models here.
