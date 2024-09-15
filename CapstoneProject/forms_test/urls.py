from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path("", views.home_view, name="forms_test_home"),
    path("forms/", views.InputModelForm, name="forms_test_input"),
 ]
 