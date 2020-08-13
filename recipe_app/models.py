from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
  name = models.CharField(max_length=80)
  bio = models.TextField(default=None)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  

class Recipe(models.Model):
  title = models.CharField(max_length=50)
  time_req = models.CharField(max_length=10, default=None)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  description = models.TextField()
  post_date = models.DateTimeField(default=timezone.now)
  instructions = models.TextField()

  def __str__(self):
    return f"{self.title} - {self.author.name}"