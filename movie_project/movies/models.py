from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    copies = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

