from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseForbidden

from recipe_app.models import Recipe, Author
from recipe_app.forms import RecipeForm, AuthorForm, LoginForm

# Matt Perry and Peter Marsh both helped with fine tuning this project

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


@login_required
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
        author=request.user.author,
      )
      return HttpResponseRedirect(reverse('home'))
  form = RecipeForm()
  return render(request, "generic_form.html", {"form": form})


@login_required
def author_form_view(request):
  if request.user.is_staff:
    if request.method == "POST":
      form = AuthorForm(request.POST)
      if form.is_valid():
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
        Author.objects.create(name=data.get("name"), bio=data.get('bio'), user=new_user)
      return HttpResponseRedirect(reverse('home'))
  else:
    return HttpResponseForbidden("You do not have permission to view this page.")
  form = AuthorForm()
  return render(request, "generic_form.html", {"form": form})


def login_view(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(request, username=data.get('username'), password=data.get('password'))
      if user:
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
  form = LoginForm()
  return render(request, "generic_form.html", {"form": form})


def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))
