from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, Ingredient, RecipeImage


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile)
