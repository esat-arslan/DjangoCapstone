from django.contrib import admin

# Register your models here.
from .models import MenuItem, Ingredient, Purchase, RecipeRequirment

admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(Purchase)
admin.site.register(RecipeRequirment)