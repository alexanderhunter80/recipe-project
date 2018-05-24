from django.db import models
from django.contrib.auth.models import User
from apps.users.models import Profile

class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        result = {
        'status' : False,
        'errors' : []
        }
        # if len(result['errors']) < 1:
        #     result['status'] = True
        #     newRecipe = Recipe.objects.create(

        #     newRecipe.save()
        return result


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    steps = models.TextField()
    notes = models.TextField(max_length=1000)
    user = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Entry(models.Model):
    qty = models.FloatField()
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name="entries", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name="entries", on_delete=models.CASCADE)

class Cookbook(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(max_length=1000)
    recipes = models.ManyToManyField(Recipe, related_name="cookbooks")
    user = models.ForeignKey(User, related_name="cookbooks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
