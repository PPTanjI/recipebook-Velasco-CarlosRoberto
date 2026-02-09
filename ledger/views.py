import json
import os
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def load_json(filename):
    file_path = os.path.join(settings.BASE_DIR, 'ledger', 'data', filename)
    with open(file_path, 'r') as file:
        return json.load(file)

def recipe_list(request):
    context = load_json('recipes_list.txt')
    return render(request, 'ledger/recipe_list.html', context)

def recipe_1(request):
    context = load_json('recipe1.txt')
    return render(request, 'ledger/recipe_detail.html', context)

def recipe_2(request):
    context = load_json('recipe2.txt')
    return render(request, 'ledger/recipe_detail.html', context)