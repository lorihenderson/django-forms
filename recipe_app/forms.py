from django import forms
from recipe_app.models import Author, Recipe

class RecipeForm(forms.Form):
  title = forms.CharField(max_length=50)
  time_req = forms.CharField(max_length=25)
  description = forms.CharField(widget=forms.Textarea)
  instructions = forms.CharField(widget=forms.Textarea)
  author = forms.ModelChoiceField(queryset=Author.objects.all())