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
    qty = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredient = models.ManyToManyField(Ingredient, related_name="recipe_id")
    step = models.TextField
    notes = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

