from django import forms
from .models import MenuItem, Ingredient, Purchase, RecipeRequirment
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
class RecipeRequirmentForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirment
        fields = "__all__"