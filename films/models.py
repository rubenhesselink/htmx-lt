from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    movie_list = models.ManyToManyField("Movie", related_name="users_with_movie_in_list")


class Movie(models.Model):
    title = models.CharField(max_length=80)
