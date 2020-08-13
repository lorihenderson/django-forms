from django import forms
from recipe_app.models import Author, Recipe

class RecipeForm(forms.Form):
  title = forms.CharField(max_length=50)
  time_req = forms.CharField(max_length=25)
  description = forms.CharField(widget=forms.Textarea)
  instructions = forms.CharField(widget=forms.Textarea)
  author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = ["name", "bio"]


class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)