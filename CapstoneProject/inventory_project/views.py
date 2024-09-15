from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, Purchase, RecipeRequirment
from .forms import MenuItemForm, IngredientForm, PurchaseForm, RecipeRequirmentForm
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def index(request):
    return render(request, 'inventory_project/index.html')


class HomeView(TemplateView):
    template_name = 'inventory_project/home.html'
    def get_context_data(self):
        context = super().get_context_data()
        context["menu_items"] = MenuItem.objects.all()
        context["ingredients"] = Ingredient.objects.all()
        context["Purchases"] = Purchase.objects.all()
        context["RecipeRequirments"] = RecipeRequirment.objects.all()
        return context
class IngredientsView(ListView):
    model = Ingredient
    template_name = 'inventory_project/ingredients.html'
class PurchasesView(ListView):
    model = Purchase
    template_name = 'inventory_project/purchases.html'
class RecipeRequirmentsView(ListView):
    model = RecipeRequirment
    template_name = 'inventory_project/recipe_requirments.html'
class MenuItemsView(ListView):
    model = MenuItem
    template_name = 'inventory_project/menu_items.html'
class IngredientsCreateView(CreateView):
    model = Ingredient
    template_name = 'inventory_project/ingredient_form.html'
    form_class = IngredientForm
    success_url = '/ingredients/'
class PurchasesCreateView(CreateView):
    model = Purchase
    template_name = 'inventory_project/purchase_form.html'
    form_class = PurchaseForm
    success_url = '/purchases/'
class RecipeRequirmentsCreateView(CreateView):
    model = RecipeRequirment
    template_name = 'inventory_project/recipe_requirment_form.html'
    form_class = RecipeRequirmentForm
    success_url = '/recipe_requirments/'
class MenuItemsCreateView(CreateView):
    model = MenuItem
    template_name = 'inventory_project/menu_item_form.html'
    form_class = MenuItemForm
    success_url = '/menu_items/'
class IngredientsUpdateView(UpdateView):
    model = Ingredient
    template_name = 'inventory_project/ingredient_form.html'
    form_class = IngredientForm
    success_url = reverse_lazy('ingredients')
class PurchasesUpdateView(UpdateView):
    model = Purchase
    template_name = 'inventory_project/purchase_form.html'
    form_class = PurchaseForm
    success_url = '/purchases/'
class RecipeRequirmentsUpdateView(UpdateView):
    model = RecipeRequirment
    template_name = 'inventory_project/recipe_requirment_form.html'
    form_class = RecipeRequirmentForm
    success_url = '/recipe_requirments/'
class MenuItemsUpdateView(UpdateView):
    model = MenuItem
    template_name = 'inventory_project/menu_item_form.html'
    form_class = MenuItemForm
    success_url = reverse_lazy('menu_items')
class IngredientsDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory_project/ingredient_confirm_delete.html'
    success_url = '/ingredients/'
class PurchasesDeleteView(DeleteView):
    model = Purchase
    template_name = 'inventory_project/purchase_confirm_delete.html'
    success_url = '/purchases/'
class RecipeRequirmentsDeleteView(DeleteView):
    model = RecipeRequirment
    template_name = 'inventory_project/recipe_requirment_confirm_delete.html'
    success_url = '/recipe_requirments/'
class MenuItemsDeleteView(DeleteView):
    model = MenuItem
    template_name = 'inventory_project/menu_item_confirm_delete.html'
    success_url = '/menu_items/'
class PurchaseDetail(DetailView):
    model = Purchase
    template_name = 'inventory_project/purchase_detail.html'
class RecipeRequirmentsDetailView(DetailView):
    model = RecipeRequirment
    template_name = 'inventory_project/recipe_requirment_detail.html'
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})