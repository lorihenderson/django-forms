from django.shortcuts import render

from recipe_app.models import Recipe, Author

# Create your views here.

def index(request):
  context = {
    "website": "Recipe Box V1",
    "author": Author.objects.all(),
    "bio": "Bio",
    "recipe": Recipe.objects.all(),
  }
  template_name = "index.html"
  return render(request, template_name, context)


def recipe_detail(request, post_id):
  the_recipes = Recipe.objects.filter(id=post_id).first()
  return render(request, "recipe_detail.html", {"post": the_recipes})


def author_details(request, author_id):
  the_authors = Author.objects.filter(id=author_id).first()
  authors_recipes = Recipe.objects.filter(author=the_authors.id)
  return render(request, "author_details.html", {"author": the_authors, "recipes": authors_recipes})