from django.db import models

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
    step = models.TextField()
    notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Entry(models.Model):
    qty = models.FloatField()
    unit = models.CharField(max_length=100)
    recipe_id = models.ForeignKey(Recipe, related_name="ingredient_entry", on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, related_name="recipe_entry", on_delete=models.CASCADE)

class Cookbook(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(max_length=1000)
    recipes = models.ManyToManyField(Recipe, related_name="cookbooks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
