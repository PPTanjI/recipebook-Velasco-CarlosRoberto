from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('<int:pk>/add_image/', views.RecipeImageCreateView.as_view(),
         name='add_image'),
]
