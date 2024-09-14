from django.db import models
from django.utils import timezone
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, blank=False)
    quantity = models.FloatField(default=0)
    unit_type_choices = [
        ('lbs', 'Pound'),
        ('oz', 'Ounce'),
        ('cups', 'Cup'),
        ('tsp', 'Teaspoon'),
        ('grm', 'Gram'),
        ('tms', 'Times'),
    ]   
    unit = models.CharField(
        max_length=4,
        choices=unit_type_choices,
        default='grm'
        )
    unit_price = models.FloatField(blank=False, default=0)
    def __str__(self):
        return f"{self.name} - ${self.unit_price:.2f} per {self.unit}"
class MenuItem(models.Model):
    title = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    def __str__(self):
        return f"{self.title} - {self.price}"
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.menu_item} - {self.timestamp}"
class RecipeRequirment(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False)
    def __str__(self):
        return f"{self.menu_item} - {self.ingredient} - {self.quantity}"
    def recipe_cost(self):
        return self.quantity * self.ingredient.unit_price