from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import RecipeForm

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

def recipe_form_view(request):
  if request.method == "POST":
    form = RecipeForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Recipe.objects.create(
        title=data.get('title'),
        time_req=data.get('time_req'),
        description=data.get('description'),
        instructions=data.get('instructions'),
        author=data.get('author'),
      )
      return HttpResponseRedirect(reverse('home'))
  form = RecipeForm()
  return render(request, "generic_form.html", {"form": form})