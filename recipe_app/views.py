from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    "author": "Author",
    "article": "Article",
  }
  template_name = "index.html"
  return render(request, template_name, context)
