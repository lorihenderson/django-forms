from django import forms
from recipe_app.models import Author, Recipe

class RecipeForm(forms.Form):
  title = forms.CharField(max_length=50)
  time_req = forms.CharField(max_length=25)
  description = forms.CharField(widget=forms.Textarea)
  instructions = forms.CharField(widget=forms.Textarea)
  # author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
  name = forms.CharField(max_length=100)
  bio = forms.CharField(max_length=100)


class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
