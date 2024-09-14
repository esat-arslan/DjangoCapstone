from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("ingredients/", views.IngredientsView.as_view(), name="ingredients"),
    path("purchases/", views.PurchasesView.as_view(), name="purchases"),
    path("recipe_requirments/", views.RecipeRequirmentsView.as_view(), name="recipe_requirments"),
    path("menu_items/", views.MenuItemsView.as_view(), name="menu_items"),
    path("ingredients/create/", views.IngredientsCreateView.as_view(), name="create_ingredient"),
    path("purchases/create/", views.PurchasesCreateView.as_view(), name="purchases_create"),
    path("recipe_requirments/create/", views.RecipeRequirmentsCreateView.as_view(), name="recipe_requirments_create"),
    path("menu_items/create/", views.MenuItemsCreateView.as_view(), name="menu_items_create"),
    path("ingredients/<int:pk>/update/", views.IngredientsUpdateView.as_view(), name="update_ingredient"),
    path("purchases/<int:pk>/update/", views.PurchasesUpdateView.as_view(), name="purchases_update"),
    path("recipe_requirments/<int:pk>/update/", views.RecipeRequirmentsUpdateView.as_view(), name="recipe_requirments_update"),
    path("menu_items/<int:pk>/update/", views.MenuItemsUpdateView.as_view(), name="menu_items_update"),
    path("ingredients/<int:pk>/delete/", views.IngredientsDeleteView.as_view(), name="delete_ingredient"),
    path("purchases/<int:pk>/delete/", views.PurchasesDeleteView.as_view(), name="purchases_delete"),
    path("recipe_requirments/<int:pk>/delete/", views.RecipeRequirmentsDeleteView.as_view(), name="recipe_requirments_delete"),
    path("menu_items/<int:pk>/delete/", views.MenuItemsDeleteView.as_view(), name="menu_items_delete"),
    path("login/", auth_views.LoginView.as_view(template_name="inventory_project/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="inventory_project/logout.html"), name="logout"),
    path('signup/', views.signup, name='signup'),  
      
    ]