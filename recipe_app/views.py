from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    "website": "Recipe Box V1",
    "author": "Author",
    "recipe": "Recipe",
  }
  template_name = "index.html"
  return render(request, template_name, context)
